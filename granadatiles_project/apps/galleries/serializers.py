from rest_framework import serializers
from core.serializers import BaseCatalogSerializer, BaseGalleryImageSerializer


class GalleryCategorySerializer(BaseCatalogSerializer):
    pass


class GallerySerializer(BaseCatalogSerializer):
    image = serializers.CharField()
    categories = GalleryCategorySerializer(many=True, required=False)


class GalleryImageSerializer(BaseGalleryImageSerializer):
    designer = serializers.StringRelatedField()
    photographer = serializers.StringRelatedField()
