from core.dtos import BaseContentDto
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