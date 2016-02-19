from rest_framework import serializers
from core.serializers import BaseContentSerializer, BaseCatalogOrderSerializer, BaseGalleryNavImageSerializer
from apps.news.serializers import SectionFeaturedArticleSerializer, ArticleMagazineSerializer
from .models import Social


class TestimonySerializer(BaseContentSerializer):
    subtitle = serializers.CharField()


class SectionSerializer(BaseContentSerializer):
    pass


class SectionCoverSerializer(serializers.Serializer):
    image = serializers.CharField()
    designer = serializers.CharField()
    photographer = serializers.CharField()
    featuredArticle = SectionFeaturedArticleSerializer(required=False)
    articles = ArticleMagazineSerializer(many=True, required=False)

class FlatPageSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    menu = serializers.IntegerField()

class FlatPageCoverSerializer(serializers.Serializer):
    image = serializers.CharField()

class FlatPageMenuSerializer(serializers.Serializer):
    title = serializers.CharField()
    url = serializers.URLField()

class CollectionContentSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    collectionId = serializers.IntegerField()
    

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        
        
class FeaturedVideoSerializer(BaseCatalogOrderSerializer):
    video = serializers.URLField()

class IndexNavigationSerializer(BaseGalleryNavImageSerializer):
    actionName = serializers.CharField()

    