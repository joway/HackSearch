from rest_framework import serializers


class SearchSerializer(serializers.Serializer):
    query = serializers.CharField()
    page = serializers.IntegerField()

    class Meta:
        fields = ('query', 'page',)


class SiteSearchSerializer(serializers.Serializer):
    site = serializers.URLField()
    query = serializers.CharField()

    class Meta:
        fields = ('query',)
