from rest_framework import serializers
from core.serializers import BaseGallerieImageSerializer


class CollectionSerializer(BaseGallerieImageSerializer):
    url = serializers.URLField()
