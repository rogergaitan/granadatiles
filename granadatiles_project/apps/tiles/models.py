from django.db import models
from apps.utils.models import BaseDescriptionImageModel

class Collection(BaseDescriptionImageModel):
    pass

class Group(BaseDescriptionImageModel):
    collection = models.ForeignKey(Collection)
  
class TileSize(models.Model):
    weight = models.IntegerField()
    thickness = models.IntegerField()
  
class Tile(BaseDescriptionImageModel):
    group = models.ForeignKey(Group)
    sizes = models.ManyToManyField(TileSize)