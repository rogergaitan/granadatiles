from .dtos import GalleryDto, GalleryCategoryDto
from .models import Gallery, GalleryCategory

class GalleryService(object):
    def get_galleries(language=None):
        galleries = Gallery.objects.all()
        galleriesDto = [GalleryDto(gallery, language=language) for gallery in galleries]
        return galleriesDto

class GalleryCategoryService(object):
    def get_gallery_category(id, language=None):
        gallery_category = GalleryCategory.objects.get(pk=id)
        gallery_categoryDto = GalleryCategoryDto(gallery_category, language=language)
        return gallery_categoryDto