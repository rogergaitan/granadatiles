from django.db import models
from apps.utils.models import BaseDescriptionImageModel, BaseNameModel

class Collection(BaseDescriptionImageModel):
    pass

class Group(BaseDescriptionImageModel):
    collection = models.ForeignKey(Collection)
  
class TileSize(models.Model):
    weight = models.IntegerField()
    thickness = models.IntegerField()
    
class PalleteColor(BaseNameModel):
    number = models.CharField(max_length=20)
  
class Tile(BaseDescriptionImageModel):
    group = models.ForeignKey(Group)
    sizes = models.ManyToManyField(TileSize)
    colors = models.ManyToManyField(PalleteColor)