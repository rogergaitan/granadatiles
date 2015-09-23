from rest_framework import serializers
from core.serializers import BaseContentSerializer, BaseCatalogOrderSerializer
from apps.news.serializers import SectionFeaturedArticleSerializer
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
    

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        
        
class FeaturedVideoSerializer(BaseCatalogOrderSerializer):
    video = serializers.URLField()