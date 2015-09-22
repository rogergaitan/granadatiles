from rest_framework import serializers
from core.serializers import BaseContentSerializer
from apps.news.serializers import FeaturedArticleSerializer
from .models import Social


class TestimonySerializer(BaseContentSerializer):
    subtitle = serializers.CharField()


class SectionSerializer(BaseContentSerializer):
	pass


class SectionCoverSerializer(serializers.Serializer):
    image = serializers.CharField()
    designer = serializers.CharField()
    photographer = serializers.CharField()
    featuredArticle = FeaturedArticleSerializer()
    

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social