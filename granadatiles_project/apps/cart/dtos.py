from core.dtos import BaseDto, BaseCatalogDto


class TileColorDto(BaseCatalogDto):

    def __init__(self, color, language, colorIsDict = False):
        if colorIsDict:
            self.name = color['color__name']
            self.id = color['color__id']
        else:
            super().__init__(color, language)


class TileDto(BaseCatalogDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.size = tile.size
        self.image = tile.image.url if tile.image else ''
        self.colors = [TileColorDto(color, language, colorIsDict=True) for color in tile.colors.values('color__id', 'color__name').distinct()]
        self.inStock = tile.in_stock()


class BaseTileOrdersDto(BaseDto):

    def __init__(self, order):
        super().__init__(order)
        self.sqFt = order.sq_ft
        self.quantity = order.quantity
        self.boxes = order.boxes
        self.subtotal = order.subtotal


class TileOrdersDto(BaseTileOrdersDto):

    def __init__(self, tile_order, language):
        super().__init__(tile_order)
        self.tile = TileDto(tile_order.tile, language)


class GroupColorDto:

    def __init__(self, group_color, language):
        self.group = group_color.group
        self.color_name = group_color.color.get_name(language)
        self.color_code = group_color.color.hexadecimalCode


class CustomizedTileOrdersDto(BaseTileOrdersDto):

    def __init__(self, customized_tile_order, language):
        super().__init__(customized_tile_order)
        self.tile = TileDto(customized_tile_order.customized_tile.tile, language)
        self.group_colors = [GroupColorDto(group_color, language)
                            for group_color in customized_tile_order.customized_tile.group_colors.all()]

class BaseSampleOrdersDto(BaseDto):

    def __init__(self, order):
        super().__init__(order)
        self.quantity = order.quantity
        self.subtotal = order.subtotal

class SampleOrdersDto(BaseSampleOrdersDto):

    def __init__(self, sample_order, language):
        super().__init__(sample_order)
        self.tile = TileDto(sample_order.tile, language)


class CustomizedSampleOrdersDto(BaseSampleOrdersDto):

    def __init__(self, customized_sample_order, language):
        super().__init__(customized_sample_order)
        self.tile = TileDto(customized_sample_order.customized_tile.tile, language)
        self.group_colors = [GroupColorDto(group_color, language)
                            for group_color in customized_sample_order.customized_tile.group_colors.all()]
