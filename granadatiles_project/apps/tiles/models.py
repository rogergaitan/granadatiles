from django.db import models
from apps.utils.models import BaseDescriptionImageModel

class Collection(BaseDescriptionImageModel):
  pass

class Group(BaseDescriptionImageModel):
  collection = models.ForeignKey(Collection)
  
class Tile(BaseDescriptionImageModel):
  group = models.ForeignKey(Group)