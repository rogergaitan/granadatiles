class BaseDto(object):

    def __init__(self, base):
        self.id = base.id


class BaseCatalogDto(BaseDto):

    def __init__(self, baseCatalog, language=None):
        super().__init__(baseOrderCatalog)
        if language:
            self.name = baseCatalog.get_name(language)
        else:
            self.name = baseCatalog.name


class BaseCatalogOrderDto(BaseCatalogDto):

    def __init__(self, baseOrderCatalog, language=None):
        super().__init__(baseOrderCatalog, language)
        self.order = baseOrderCatalog.order


class BaseContentDto(BaseDto):

    def __init__(self, baseContent, language=None):
        super().__init__(baseContent)
        if language:
            self.title = baseContent.get_title(language)
            self.description = baseContent.get_description(language)
        else:
            self.title = baseContent.title
            self.description = baseContent.description


class BaseContentOrderDto(BaseContentDto):

    def __init__(self, baseContentOrder, language=None):
        super().__init__(baseContentOrder, language)
        self.order = baseContentOrder.order


class BaseGalleryImageDto(BaseContentDto):

    def __init__(self, baseGalleryImage, language=None):
        self.image = baseGalleryImage.image.url if baseGalleryImage.image else ''
        super().__init__(baseGalleryImage, language)


class BaseGallerieNavImageModel(BaseGalleryImageDto):

    def __init__(self, baseGalleryNavImage, language=None):
        super().__init__(baseGalleryNavImage, language)
        self.target = baseGalleryNavImage.target
        self.link = baseGalleryNavImage.link
