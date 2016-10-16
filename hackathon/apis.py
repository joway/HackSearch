from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from elastic.services import ElasticService
from hackathon.serializers import SearchSerializer, SiteSearchSerializer
from utils.helpers import get_root_domain


class HackViewSet(viewsets.GenericViewSet):
    serializer_class = SearchSerializer
    permission_classes = [AllowAny, ]

    @list_route(methods=['GET'])
    def search(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        data = ElasticService.search(index='tech', body={
            "query": {"match": {'content': data['query']}},
            "highlight": {"fields": {"content": {}}}
        })
        return Response(data, status=status.HTTP_201_CREATED)

    @list_route(methods=['GET'])
    def site_search(self, request, *args, **kwargs):
        serializer = SiteSearchSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        data = ElasticService.search(index='tech',
                                     doc_type=get_root_domain(data['site']),
                                     body={
                                         "query": {"match": {'content': data['query']}},
                                         "highlight": {"fields": {"content": {}}}
                                     })
        return Response(data, status=status.HTTP_200_OK)
