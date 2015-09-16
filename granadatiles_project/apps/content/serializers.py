from rest_framework import serializers
from core.serializers import BaseContentSerializer


class TestimonySerializer(BaseContentSerializer):
    subtitle = serializers.CharField()

class SectionSerializer(BaseContentSerializer):
	pass