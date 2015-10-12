class BaseDto(object):
    
    def __init__(self, model):
        self.id = model.id


class BaseCatalogDto(BaseDto):

    def __init__(self, baseCatalogModel, language=None):
        super().__init__(baseCatalogModel)
        if language:
            self.name = baseCatalogModel.get_name(language)
        else:
            self.name = baseCatalogModel.name


class BaseCatalogOrderDto(BaseCatalogDto):

    def __init__(self, baseOrderCatalogModel, language=None):
        super().__init__(baseOrderCatalogModel, language)
        self.order = baseOrderCatalogModel.order


class BaseContentDto(BaseDto):

    def __init__(self, baseContentModel, language=None):
        super().__init__(baseContentModel)
        if language:
            self.title = baseContentModel.get_title(language)
            self.description = baseContentModel.get_description(language)
        else:
            self.title = baseContentModel.title
            self.description = baseContentModel.description


class BaseContentOrderDto(BaseContentDto):

    def __init__(self, baseContentOrderModel, language=None):
        super().__init__(baseContentOrderModel, language)
        self.order = baseContentOrderModel.order


class BaseGalleryImageDto(BaseContentDto):

    def __init__(self, baseGalleryImageModel, language=None):
        self.image = baseGalleryImageModel.image.url if baseGalleryImageModel.image else ''
        super().__init__(baseGalleryImageModel, language)


class BaseGalleryNavImageModel(BaseGalleryImageDto):

    def __init__(self, baseGalleryNavImageModel, language=None):
        super().__init__(baseGalleryNavImageModel, language)
        self.target = baseGalleryNavImageModel.target
        self.link = baseGalleryNavImageModel.link
