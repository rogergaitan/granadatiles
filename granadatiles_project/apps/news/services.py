from .dtos import CatalogDto
from .models import Catalog


class CatalogService(object):
    
    def get_catalogs(language=None):
        catalogs = Catalog.objects.all()
        catalogsDto = [CatalogDto(catalog, language=language) for catalog in catalogs]
        return catalogsDto