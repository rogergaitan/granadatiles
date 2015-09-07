﻿from django.db import models
from django.utils.translation import ugettext as _
from sorl.thumbnail import ImageField


def model_directory_path(instance, filename):
    return instance.__class__.__name__ + '/' + filename


class BaseCatalogModel(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('Name'))

    name_es = models.CharField(max_length=150, verbose_name=_('Name'),
                               blank=True,
                               null=True)

    def get_name(self, language):
        if language == 'es' and self.title_es is not None and self.title_es:
            return self.title_es
        return self.title

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class BaseCatalogOrderModel(BaseCatalogModel):
    order = models.PositiveIntegerField(unique=True, verbose_name='Order')

    class Meta:
        abstract = True


class BaseContentModel(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('Title'))

    title_es = models.CharField(max_length=160,
                                blank=True,
                                null=True)

    description = models.TextField(verbose_name=_('Description'))

    description_es = models.TextField(blank=True,
                                      null=True)

    def get_title(self, language):
        if language == 'es' and self.title_es is not None and self.title_es:
            return self.title_es
        return self.title

    def get_description(self, language):
        if language == 'es' and self.description_es is not None and self.description_es:
            return self.description_es
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class BaseContentOrderModel(BaseContentModel):
    order = models.PositiveIntegerField(unique=True, verbose_name='Order')

    class Meta:
        abstract = True


class BaseGallerieImageModel(BaseContentModel):
    image = ImageField(
        upload_to=model_directory_path, verbose_name=_('Image'))

    class Meta:
        abstract = True


class BaseGallerieNavImageModel(BaseGallerieImageModel):
    target = models.BooleanField(default=False, help_text=_('Open in new tab'))
    link = models.URLField(blank=True, null=True, verbose_name=_('Link'))

    class Meta:
        abstract = True