from rest_framework import serializers
from core.serializers import BaseGalleryImageSerializer


class CollectionSerializer(BaseGalleryImageSerializer):
    url = serializers.URLField()

class GroupSerializer(BaseGalleryImageSerializer):
    pass

class MenuCollectionSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()
    url = serializers.URLField()