from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from w3lib.url import canonicalize_url

from elastic.services import ElasticService
from project.models import Project
from project.serializers import ProjectCreateSerializer, ProjectResultSerializer, ProjectSerializer
from project.services import ProjectService
from spider.scheduler.tasks import scheduling


class RetrieveType(object):
    NORMAL = 'normal'
    ELASTIC = 'elastic'


class ProjectViewSet(viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectCreateSerializer
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        proj = serializer.save()
        proj.entry_url = canonicalize_url(proj.entry_url)
        proj.save()

        scheduling.delay(proj_id=proj.proj_id,
                         links=[proj.entry_url],
                         options=ProjectService.gen_project_options(proj))
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        retrieve_type = request.GET.get('type', RetrieveType.NORMAL)
        if retrieve_type == RetrieveType.NORMAL:
            return Response(ProjectSerializer(instance=instance).data,
                            status=status.HTTP_200_OK)

        if retrieve_type == RetrieveType.ELASTIC:
            data = ElasticService.search(index=instance.catalog, doc_type=instance.proj_id)
            serializer = ProjectResultSerializer(data={'proj_id': instance.proj_id, 'results': data})
            serializer.is_valid(raise_exception=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({'error': 'illegal type'}, status=status.HTTP_201_CREATED)
