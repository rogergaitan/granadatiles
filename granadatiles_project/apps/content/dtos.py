import random
from core.dtos import BaseContentDto


class TestimonyDto(BaseContentDto):

    def __init__(self, testimony, language=None):
        super().__init__(testimony, language)
        if language:
            self.subtitle = testimony.get_subtitle(language)
        else:
            self.subtitle = testimony.get_subtitle()
            
class SectionCoverDto(object):
    
    def __init__(self, section):
        
        if section.images.count() > 1:
            self.image = self.get_random_cover(section)
        elif section.images.count() == 1:
            self.image = section.images.first()
        else:
            self.image = ''
        
        if self.image:
            self.cover = self.image.image
            self.designer = self.image.designer
            self.photographer = self.image.photographer
        else:
            self.cover = ''
            self.designer = ''
            self.photographer = ''
        
    def get_random_cover(self, section):
        ids = section.images.values_list('id')
        choice = random.sample(list(ids), 1)
        image = section.images.get(pk=choice[0][0])
        return image