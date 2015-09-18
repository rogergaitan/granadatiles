from rest_framework import serializers
from core.serializers import BaseCatalogSerializer

class GallerySerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    categories = serializers.StringRelatedField(many=True)