from django.shortcuts import render
from rest_framework import generics
from .serializers import CollectionSerializer, TileSerializer, GroupSerializer
from .models import Collection, Tile, Group

class CollectionList(generics.ListAPIView):
	queryset = Collection.objects.all()
	serializer_class = CollectionSerializer

class TileList(generics.ListAPIView):
	queryset = Tile.objects.all()
	serializer_class = TileSerializer
	
class GroupList(generics.ListAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer