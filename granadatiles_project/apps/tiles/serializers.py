from rest_framework import serializers
from .models import Collection, Tile, Group


class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		
class CollectionSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    
    def get_title(self, obj):
        return obj.get_title(self.context['request'].LANGUAGE_CODE)
    
    def get_description(self, obj):
        return obj.get_description(self.context['request'].LANGUAGE_CODE)
    
    class Meta:
        model = Collection
        fields = ('title', 'description', 'image')

class CollectionGroupSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
	
    class Meta:
        model = Collection

class TileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tile