from rest_framework import serializers
from core.serializers import BaseGalleryImageSerializer, BaseCatalogSerializer


class SectionFeaturedArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.CharField()
    url = serializers.URLField()
    

class ArticleMagazineSerializer(serializers.Serializer):
    url = serializers.URLField()
    magazineName = serializers.CharField()
    magazineLogo = serializers.CharField()
    

class ArticleYearSerializer(serializers.Serializer):
    year = serializers.CharField()
    
    
class ArticleSerializer(BaseGalleryImageSerializer):
    date = serializers.CharField()
    magazine = serializers.CharField()


class CatalogSerializer(BaseCatalogSerializer):
    file = serializers.CharField()
    image = serializers.CharField()