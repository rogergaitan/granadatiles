from django.db import models
from core.models import BaseGallerieImageModel, BaseCatalogModel, BaseContentModel

class TileSize(models.Model):
    weight = models.IntegerField()
    thickness = models.IntegerField()
    
class PalleteColor(BaseCatalogModel):
    hexadecimalCode = models.CharField(max_length=20)


class Collection(BaseGallerieImageModel):
    pass

class Group(BaseGallerieImageModel):
    collection = models.ForeignKey(Collection)
  
class Tile(BaseContentModel):
    group = models.ForeignKey(Group)
    sizes = models.ManyToManyField(TileSize)
    colors = models.ManyToManyField(PalleteColor)