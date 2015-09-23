from core.dtos import BaseContentDto, BaseCatalogDto 


class SectionFeaturedArticleDto(object):
    
    def __init__(self, article, language = None):
        self.title = article.get_title(language)
        self.image = article.image
        self.url = article.url


class CatalogDto(BaseCatalogDto):
   def __init__(self, catalog, language=None):
       super().__init__(catalog, language)
       self.file = catalog.file
       self.image = catalog.image