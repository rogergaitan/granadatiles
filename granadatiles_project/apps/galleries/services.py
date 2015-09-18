from .dtos import GalleryDto
from .models import Gallery

class GalleryService(object):
    def get_galleries(language=None):
        galleries = Gallery.objects.all()
        galleriesDto = [GalleryDto(gallery, language=language) for gallery in galleries]
        return galleriesDto
