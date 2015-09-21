from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from core.views import BaseViewSet
from .serializers import GallerySerializer, GalleryCategorySerializer, GalleryImageSerializer
from .services import GalleryService, GalleryCategoryService


def galleries(request):
    return render(request, 'galleries/galleries_list.html')


class GalleryViewSet(BaseViewSet):
    
    def list(self, request):
       galleries = GalleryService.get_galleries(language=self.get_language(request))
       serializer = GallerySerializer(galleries, many=True)
       return Response(serializer.data)
   
   
class GalleryCategoryViewSet(BaseViewSet):
    
    @detail_route(methods=['get'])
    def images(self, request, pk=None):
        images = GalleryCategoryService.get_images(
                               gallery_category_id=pk,
                               language=self.get_language(request))
        serializer = GalleryImageSerializer(images, many=True)
        return Response(serializer.data)