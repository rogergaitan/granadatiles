from core.dtos import BaseContentDto, BaseCatalogOrderDto
from apps.news.dtos import ArticleDto


class TestimonyDto(BaseContentDto):

    def __init__(self, testimony, language=None):
        super().__init__(testimony, language)
        if language:
            self.subtitle = testimony.get_subtitle(language)
        else:
            self.subtitle = testimony.get_subtitle()
            
            
class SectionCoverDto(object):
    
    def __init__(self, section_image):
        
        self.image = section_image.image
        self.designer = section_image.designer
        self.photographer = section_image.photographer
        self.featuredArticle = ArticleDto
        
class FeaturedVideoDto(BaseCatalogOrderDto):

   def __init__(self, featured_video, language=None):
       super().__init__(featured_video, language)
       self.video = featured_video.video