from django.shortcuts import render
from rest_framework import generics
from .serializers import CollectionSerializer, CollectionGroupSerializer, TileSerializer, GroupSerializer
from .models import Collection, Tile, Group


class CollectionList(generics.ListAPIView):
	queryset = Collection.objects.all()
	serializer_class = CollectionSerializer
	

class CollectionDetail(generics.RetrieveAPIView):
	queryset = Collection.objects.all()
	serializer_class = CollectionGroupSerializer
	

class TileList(generics.ListAPIView):
	queryset = Tile.objects.all()
	serializer_class = TileSerializer

	
class GroupList(generics.ListAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	
	
class GroupDetail(generics.RetrieveAPIView):
	queryset = Group.objects.all()
	serializer_class = GroupSerializer