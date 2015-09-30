from core.dtos import BaseCatalogDto, BaseGalleryImageDto


class GalleryCategoryDto(BaseCatalogDto):
    pass


class GalleryDto(BaseCatalogDto):
	
    def __init__(self, gallery, language=None):
        super().__init__(gallery, language)
        self.image = gallery.image.url
        self.categories = gallery.categories.all()
        
    
class GalleryImageDto(BaseGalleryImageDto):
    
    def __init__(self, image, language=None):
       super().__init__(image, language)
       self.designer = image.designer
       self.photographer = image.photographer