from rest_framework import serializers
from core.serializers import BaseGallerieImageSerializer, BaseCatalogSerializer

class SectionFeaturedArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.ImageField()
    url = serializers.URLField()


class CatalogSerializer(BaseCatalogSerializer):
    file = serializers.CharField()
    image = serializers.CharField()