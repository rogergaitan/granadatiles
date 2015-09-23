from .dtos import CatalogDto, ArticleYearDto
from .models import Catalog, Article


class CatalogService(object):
    
    def get_catalogs(language=None):
        catalogs = Catalog.objects.all()
        catalogsDto = [CatalogDto(catalog, language=language) for catalog in catalogs]
        return catalogsDto
	
	
class ArticleService(object):
    def get_years():
        years = Article.objects.dates('date', 'year').reverse()
        years_choice = [ArticleYearDto(year_choice.year) for year_choice in years]
        return years_choice