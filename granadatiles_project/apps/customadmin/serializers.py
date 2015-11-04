from rest_framework import serializers

from core.serializers import BaseCatalogSerializer

class ItemCountSerializer(serializers.Serializer):
    collections = serializers.CharField()
    groups = serializers.CharField()
    tiles = serializers.CharField()
    users = serializers.CharField()


class LatestTilesSerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    url = serializers.CharField()


class LatestUsersSerializer(serializers.Serializer):
    name = serializers.CharField()
    url = serializers.CharField()
