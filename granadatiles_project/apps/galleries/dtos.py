from core.dtos import BaseCatalogDto, BaseGalleryImageDto


class GalleryCategoryDto(BaseCatalogDto):
    pass


class GalleryDto(BaseCatalogDto):

    def __init__(self, gallery, language=None):
        super().__init__(gallery, language)
        self.image = gallery.image.url if gallery.image else ''
        if gallery.categories.filter(images__isnull=False):
            self.categories = [GalleryCategoryDto(category, language)
                                  for category in gallery.categories.filter(images__isnull=False).distinct()]


class GalleryImageDto(BaseGalleryImageDto):

    def __init__(self, image, language=None):
       super().__init__(image, language)
       self.designer = image.designer
       self.photographer = image.photographer
