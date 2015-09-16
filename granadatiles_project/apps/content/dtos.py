from core.dtos import BaseContentDto


class TestimonyDto(BaseContentDto):

    def __init__(self, testimony, language=None):
        super().__init__(testimony, language)
        if language:
            self.subtitle = testimony.get_subtitle(language)
        else:
            self.subtitle = testimony.get_subtitle()