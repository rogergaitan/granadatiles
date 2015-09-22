from core.dtos import BaseContentDto, BaseCatalogDto 


class ArticleDto(BaseContentDto):
    pass


class CatalogDto(BaseCatalogDto):
   def __init__(self, catalog, language=None):
       super().__init__(catalog, language)
       self.file = catalog.file
       self.image = catalog.image