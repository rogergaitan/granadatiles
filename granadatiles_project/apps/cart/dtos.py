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

#TODO add price field
class TileOrdersDto(BaseDto):

    def __init__(self, tileorder, language):
        super().__init__(tileorder)
        self.sq_ft = tileorder.sq_ft
        self.quantity = tileorder.quantity
        self.boxes = tileorder.boxes
        self.tile = TileDto(tileorder.tiles, language)


class SampleOrdersDto(BaseDto):

    def __init__(self, sampleorder, language):
        super().__init__(sampleorder)
        self.quantity = sampleorder.quantity
        self.tile = TileDto(sampleorder.tiles, language)
