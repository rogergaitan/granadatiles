from django.shortcuts import render
from rest_framework.response import Response
from core.views import BaseViewSet
from .serializers import CatalogSerializer
from .services import CatalogService

def news(request):
    return render(request, 'news/article_list.html')


class CatalogViewSet(BaseViewSet):
    
    def list(self, request):
       catalogs = CatalogService.get_catalogs(language=self.get_language(request))
       serializer = CatalogSerializer(catalogs, many=True)
       return Response(serializer.data)
   