from rest_framework import serializers
from .models import Collection, Tile, Group


class CollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Collection


class TileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tile
		

class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group