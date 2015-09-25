from rest_framework import serializers
from core.serializers import BaseCatalogSerializer, BaseGalleryImageSerializer

class GallerySerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    categories = serializers.StringRelatedField(many=True)
    

class GalleryCategorySerializer(BaseCatalogSerializer):
    pass


class GalleryImageSerializer(BaseGalleryImageSerializer):
    designer = serializers.StringRelatedField()
    photographer = serializers.StringRelatedField()