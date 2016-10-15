from rest_framework import serializers

from project.models import Project


class ProjectOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('rules', 'payload', 'process_type', 'http_method', 'headers', 'cookies')


class ProjectCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('proj_id', 'name', 'entry_url', 'rules', 'catalog', 'process_type')


class ProjectCallbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('proj_id', 'task_id', 'links', 'status')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project


class ProjectResultSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    proj_id = serializers.CharField()
    results = serializers.JSONField()
