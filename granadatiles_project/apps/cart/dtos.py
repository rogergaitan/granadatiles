from core.dtos import BaseDto, BaseCatalogDto


class TileCartDto(BaseCatalogDto):

    def __init__(self, tile, language):
        super().__init__(tile, language)
        self.image = tile.mosaic.url if tile.mosaic else ''
        self.colors = tile.colors.values('name')


class CartDto(BaseDto):

    def __init__(self, cart, language):
        super().__init__(cart)
        self.square_ft = cart.square_ft
        self.quantity = cart.quantity
        self.boxes = cart.boxes
        self.tiles = [TileCartDto(tile, language) for tile in cart.tiles.all() ]
