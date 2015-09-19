from core.dtos import BaseCatalogDto


class GalleryDto(BaseCatalogDto):
    
    def __init__(self, gallery, language=None):
        super().__init__(gallery, language)
        self.image = gallery.image
        self.categories = gallery.categories.values('name', 'id')
        
        
class GalleryCategoryDto(BaseCatalogDto):
    
    def __init__(self, gallery_category, language=None):
        super().__init__(gallery_category, language)  