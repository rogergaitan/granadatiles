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
            self.image = section.images.get(pk=random.randrange(1, section.images.count() + 1)) #Obtain random image if many
        elif section.images.count() == 1:
            self.image = section.images.first()
        else:
            self.image = ''
    
        self.designer = self.image.designer if self.image else ''
    
        self.photographer = self.image.photographer if self.image else ''