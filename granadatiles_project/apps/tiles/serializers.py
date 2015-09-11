from rest_framework import serializers
from core.serializers import BaseGallerieImageSerializer


class CollectionSerializer(BaseGallerieImageSerializer):
    url = serializers.URLField()

class GroupSerializer(BaseGallerieImageSerializer):
    pass

class MenuCollectionSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()
    url = serializers.URLField()