from django.db import models
from apps.utils.methods import model_directory_path


class BaseModel(models.Model):
    title = models.CharField(max_length=160)

    title_es = models.CharField(max_length=160,
                                blank=True,
                                null=True
                                )
    title_pr = models.CharField(max_length=160,
                                blank=True,
                                null=True
                                )

    def get_title(self, language):
        if language == 'es' and self.title_es is not None and self.title_es:
            return self.title_es
        elif language == 'pr' and self.title_pr is not None and self.title_pr:
            return self.title_pr
        return self.title

    class Meta:
        abstract = True


class BaseDescriptionImageModel(BaseModel):
    image = BaseModel.ImageField(upload_to=model_directory_path)
    description = models.TextField()

    description_es = models.TextField(blank=True,
                                      null=True)
    description_pr = models.TextField(blank=True,
                                      null=True)

    def get_description(self, language):
        if language == 'es' and self.description_es is not None and self.description_es:
            return self.description_es
        elif language == 'pr' and self.description_pr is not None and self.description_pr:
            return self.description_pr
        return self.title

    class Meta:
        abstract = True


class BaseImageModel(BaseModel):
    image = BaseModel.ImageField(upload_to=model_directory_path)

    class Meta:
        abstract = True


class BaseDescriptionModel(BaseModel):
    description = models.TextField()

    description_es = models.TextField(blank=True,
                                      null=True)
    description_pr = models.TextField(blank=True,
                                      null=True)

    def get_description(self, language):
        if language == 'es' and self.description_es is not None and self.description_es:
            return self.description_es
        elif language == 'pr' and self.description_pr is not None and self.description_pr:
            return self.description_pr
        return self.title

    class Meta:
        abstract = True
