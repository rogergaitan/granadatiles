from rest_framework import serializers
from core.serializers import BaseGallerieImageSerializer, BaseCatalogSerializer

class FeaturedArticleSerializer(BaseGallerieImageSerializer):
	pass


class CatalogSerializer(BaseCatalogSerializer):
    file = serializers.CharField()
    image = serializers.CharField()