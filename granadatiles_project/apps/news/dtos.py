from core.dtos import BaseContentDto, BaseCatalogDto, BaseGalleryImageDto


class SectionFeaturedArticleDto(object):

    def __init__(self, article, language=None):
        self.title = article.get_title(language)
        self.image = article.magazine.logo.url if article.magazine.logo.url else ''
        self.url = article.url


class ArticleMagazineDto(object):

    def __init__(self, article):
        self.url = article.url
        self.magazineName = article.magazine.name
        self.magazineLogo = article.magazine.logo.url


class ArticleYearDto(object):
    
    def __init__(self, years_choice):
        self.year = years_choice


class ArticleDto(BaseGalleryImageDto):
    
    def __init__(self, article, language=None):
       super().__init__(article, language)
       self.date = article.date
       self.magazine = article.magazine.name
       if article.url:
           self.url = article.url
       else:
           self.url = article.file.url if article.file else ''
           

class CatalogDto(BaseCatalogDto):
   
   def __init__(self, catalog, language=None):
       super().__init__(catalog, language)
       self.file = catalog.file.url if catalog.file else ''
       self.image = catalog.image.url


class CatalogPageDto:
     
    def __init__(self, page):
        self.pageNumber = page.page_number
        self.image = page.image.url if page.image else ''
   