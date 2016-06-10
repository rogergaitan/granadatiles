from django.shortcuts import get_object_or_404
from .dtos import GalleryDto, GalleryImageDto, GalleryCategoryDto
from .models import Gallery, GalleryCategory


class GalleryService(object):
    def get_galleries(language=None):
        galleries = Gallery.objects.order_by('-id')
        galleriesDto = [GalleryDto(gallery, language=language) for gallery in galleries]
        return galleriesDto

class GalleryCategoryService(object):
    def get_images(gallery_category_id, language=None):
        gallery = get_object_or_404(GalleryCategory, pk=gallery_category_id)
        images = gallery.images.all()
        imagesDto = [GalleryImageDto(image, language) for image in images]
        return imagesDto
