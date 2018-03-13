from django.shortcuts import get_object_or_404

from .dtos import CatalogDto, ArticleYearDto, ArticleDto, CatalogPageDto
from .models import Catalog, Article


class CatalogService(object):
    
    def get_catalogs(language=None):
        catalogs = Catalog.objects.all()
        catalogsDto = [CatalogDto(catalog, language=language) for catalog in catalogs]
        return catalogsDto
      
    def get_page_catalogs(pk):
        catalog = get_object_or_404(Catalog.objects.prefetch_related('pages'),  pk=pk)
        page_catalogsDto = [CatalogPageDto(page) for page in catalog.pages.all()]
        return page_catalogsDto


class ArticleService(object):
	
    def get_articles(year, language=None):
        articles = Article.objects.select_related('magazine')
        
        if year: articles = articles.filter(date__year=year)
            
        articlesDto = [ArticleDto(article, language=language) for article in articles]
        return articlesDto


    def get_years():
        years = Article.objects.dates('date', 'year').reverse()
        years_choiceDto = [ArticleYearDto(year_choice.year) for year_choice in years]
        return years_choiceDto