from core.dtos import BaseDto, BaseCatalogDto


class TileColorDto(BaseCatalogDto):

    def __init__(self, color, language):
        super().__init__(color, language)


class TileDto(BaseCatalogDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.list_id = tile.list_id
        self.size = tile.size
        self.image = tile.mosaic.url if tile.mosaic else ''
        self.colors = [TileColorDto(color, language) for color in tile.colors.all()]


class BaseOrderDto(BaseDto):

    def __init__(self, order):
        super().__init__(order)
        self.sq_ft = order.sq_ft
        self.quantity = order.quantity
        self.boxes = order.boxes
        self.subtotal = order.subtotal


class TileOrdersDto(BaseOrderDto):

    def __init__(self, tile_order, language):
        super().__init__(tile_order)
        self.tile = TileDto(tile_order.tile, language)


class GroupColorDto:

    def __init__(self, group_color, language):
        self.group = group_color.group
        self.color_name = group_color.color.get_name(language)
        self.color_code = group_color.color.hexadecimalCode


class CustomizedTileOrdersDto(BaseOrderDto):

    def __init__(self, customized_tile_order, language):
        super().__init__(customized_tile_order)
        self.tile = TileDto(customized_tile_order.customized_tile.tile, language)
        self.group_colors = [GroupColorDto(group_color, language)
                            for group_color in customized_tile_order.customized_tile.group_colors.all()]

class SampleOrdersDto(BaseDto):

    def __init__(self, sampleorder, language):
        super().__init__(sampleorder)
        self.quantity = sampleorder.quantity
        self.subtotal = sampleorder.subtotal
        self.tile = TileDto(sampleorder.tile, language)
