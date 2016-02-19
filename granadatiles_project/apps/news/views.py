from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from core.views import BaseViewSet
from .serializers import CatalogSerializer, ArticleYearSerializer, ArticleSerializer
from .services import CatalogService, ArticleService


def news(request):
    return render(request, 'news/article_list.html')


def catalogs(request):
    return render(request, 'news/catalogs_list.html')


class CatalogViewSet(BaseViewSet):

    def list(self, request):
        catalogs = CatalogService.get_catalogs(language=self.get_language(request))
        serializer = CatalogSerializer(catalogs, many=True)

        return Response(serializer.data)


class ArticleViewSet(BaseViewSet):

    def list(self, request):
        year = request.query_params.get('year')
        articles = ArticleService.get_articles(year=year, language=self.get_language(request))
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def years(self, request):
        years_choice = ArticleService.get_years()
        serializer = ArticleYearSerializer(years_choice, many=True)

        return Response(serializer.data)
