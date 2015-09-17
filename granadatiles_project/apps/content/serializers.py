from rest_framework import serializers
from core.serializers import BaseContentSerializer
from .models import Social

class TestimonySerializer(BaseContentSerializer):
    subtitle = serializers.CharField()

class SectionSerializer(BaseContentSerializer):
	pass

class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social