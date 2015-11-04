from rest_framework import serializers

class ItemCountSerializer(serializers.Serializer):
    collections = serializers.CharField()
    groups = serializers.CharField()
    tiles = serializers.CharField()
    users = serializers.CharField()
