from django.db import models
from apps.utils.methods import model_directory_path


class BaseModel(models.Model):
    title = models.CharField(max_length=160)

    class Meta:
        abstract = True


class BaseDescriptionImageModel(BaseModel):
    image = BaseModel.ImageField(upload_to=model_directory_path)
    description = models.TextField()

    class Meta:
        abstract = True
