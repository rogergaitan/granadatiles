from core.dtos import BaseDto, BaseCatalogDto


class TileColorDto(BaseCatalogDto):

    def __init__(self, color, language):
        super().__init__(color, language)


class TileCartDto(BaseCatalogDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.image = tile.mosaic.url if tile.mosaic else ''
        self.colors = [TileColorDto(color, language) for color in tile.colors.all()]


class CartDto(BaseDto):

    def __init__(self, cart, language):
        super().__init__(cart)
        self.square_ft = cart.square_ft
        self.quantity = cart.quantity
        self.boxes = cart.boxes
        self.tiles = [TileCartDto(tile, language) for tile in cart.tiles.all() ]
