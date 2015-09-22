from .dtos import GalleryDto, GalleryImageDto
from .models import Gallery, GalleryCategory


class GalleryService(object):
    def get_galleries(language=None):
        galleries = Gallery.objects.all()
        galleriesDto = [GalleryDto(gallery, language=language) for gallery in galleries]
        return galleriesDto

class GalleryCategoryService(object):
    def get_images(gallery_category_id, language=None):
        images = GalleryCategory.objects.get(pk=gallery_category_id).images.all()
        imagesDto = [GalleryImageDto(image, language) for image in images]
        return imagesDto