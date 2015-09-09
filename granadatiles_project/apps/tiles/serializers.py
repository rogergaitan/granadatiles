from rest_framework import serializers
from .models import Collection, Tile, Group


class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		
class CollectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Collection

class CollectionGroupSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
	
    class Meta:
        model = Collection

class TileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tile