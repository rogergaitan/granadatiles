from django.db import models

class BaseModel(models.Model):
    title = models.CharField(max_length=30)
  
    class Meta:
        abstract = True
        
class Collection(BaseModel):
  pass

class Tile(BaseModel):
  collection = models.ForeignKey(Collection)