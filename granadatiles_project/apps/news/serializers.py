﻿from rest_framework import serializers
from core.serializers import BaseGallerieImageSerializer, BaseCatalogSerializer

class SectionFeaturedArticleSerializer(serializers.Serializer):
    title = serializers.CharField()
    image = serializers.ImageField()
    url = serializers.URLField()
    

class ArticleMagazineSerializer(serializers.Serializer):
    url = serializers.URLField()
    magazineName = serializers.CharField()
    magazineLogo = serializers.CharField()


class CatalogSerializer(BaseCatalogSerializer):
    file = serializers.CharField()
    image = serializers.CharField()