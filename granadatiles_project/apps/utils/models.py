from django.db import models
from apps.utils.methods import model_directory_path
from sorl.thumbnail import ImageField

class BaseModel(models.Model):
    title = models.CharField(max_length=160)
    title_es = models.CharField(max_length=160, blank=True, null=True)

    def get_title(self, language):
        if language == 'es' and self.title_es is not None and self.title_es:
            return self.title_es
        return self.title

    class Meta:
        abstract = True


class BaseDescriptionImageModel(BaseModel):
    image = ImageField(upload_to=model_directory_path)
    description = models.TextField()
    description_es = models.TextField(blank=True, null=True)

    def get_description(self, language):
        if language == 'es' and self.description_es is not None and self.description_es:
            return self.description_es
        return self.title

    class Meta:
        abstract = True


class BaseImageModel(BaseModel):
    image = ImageField(upload_to=model_directory_path)

    class Meta:
        abstract = True


class BaseDescriptionModel(BaseModel):
    description = models.TextField()
    description_es = models.TextField(blank=True, null=True)

    def get_description(self, language):
        if language == 'es' and self.description_es is not None and self.description_es:
            return self.description_es
        return self.title

    class Meta:
        abstract = True


class BaseSectionModel(BaseDescriptionModel):
    name = models.CharField(max_length=160)
    name_es = models.CharField(max_length=160, blank=True, null=True)

    def get_name(self, language):
        if language == 'es' and self.name_es is not None and self.name_es:
            return self.name_es
        return self.title

    class Meta:
        abstract = True


class BaseNameModel(models.Model):
    name = models.CharField(max_length=160)
    name_es = models.CharField(max_length=160, blank=True, null=True)

    def get_name(self, language):
        if language == 'es' and self.name_es is not None and self.name_es:
            return self.name_es
        return self.title

    class Meta:
        abstract = True


class BaseMessageNameModel(BaseModel):
    message = models.TextField()
    message_es = models.TextField(blank=True,null=True)

    def get_description(self, language):
        if language == 'es' and self.message_es is not None and self.message_es:
            return self.message_es
        return self.title

    class Meta:
        abstract = True


class BaseMagazineModel(BaseDescriptionImageModel):
    name = models.CharField(max_length=160)
    name_es = models.CharField(max_length=160, blank=True, null=True)

    def get_name(self, language):
        if language == 'es' and self.name_es is not None and self.name_es:
            return self.name_es
        return self.title

    class Meta:
        abstract = True