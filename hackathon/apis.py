from rest_framework import serializers
from rest_framework import viewsets, status
from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from elastic.services import ElasticService


class SearchSerializer(serializers.Serializer):
    query = serializers.CharField()
    page = serializers.IntegerField()

    class Meta:
        fields = ('query', 'page',)


class HackViewSet(viewsets.GenericViewSet):
    serializer_class = SearchSerializer
    permission_classes = [AllowAny, ]

    @list_route(methods=['GET'])
    def search(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        data = ElasticService.search(query=data['query'], index='tech')
        return Response(data, status=status.HTTP_201_CREATED)
