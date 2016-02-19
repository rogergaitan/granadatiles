from .dtos import CatalogDto, ArticleYearDto, ArticleDto
from .models import Catalog, Article


class CatalogService(object):
    
    def get_catalogs(language=None):
        catalogs = Catalog.objects.all()
        catalogsDto = [CatalogDto(catalog, language=language) for catalog in catalogs]
        return catalogsDto


class ArticleService(object):
	
    def get_articles(year, language=None):
        articles = Article.objects.select_related('magazine').order_by('-date')
        
        if year:
            articles = articles.filter(date__year=year)
            
        articlesDto = [ArticleDto(article, language=language) for article in articles]
        return articlesDto


    def get_years():
        years = Article.objects.dates('date', 'year').reverse()
        years_choice = [ArticleYearDto(year_choice.year) for year_choice in years]
        return years_choice