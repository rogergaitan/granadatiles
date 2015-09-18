from django.shortcuts import render
from rest_framework.response import Response
from core.views import BaseViewSet
from .serializers import GallerySerializer
from .services import GalleryService


def galleries(request):
    return render(request, 'galleries/galleries_list.html')


class GalleryViewSet(BaseViewSet):
    
    def list(self, request):
       galleries = GalleryService.get_galleries(language=self.get_language(request))
       serializer = GallerySerializer(galleries, many=True)
       return Response(serializer.data)