# -*- encoding: utf-8 -*-

from django.db import models
from apps.utils.models import BaseModel, BaseImageModel, BaseDescriptionImageModel
from django.utils.translation import ugettext as _

# Create your models here.


class Gallery(BaseImageModel):

	class Meta:
		verbose_name = _('Gallery')
		verbose_name_plural = _('Galleries')

	def __str__(self):
		return self.title


class GalleryOptions(BaseModel):
	gallery = models.ForeignKey(Gallery, verbose_name='Gallery')

	class Meta:
		verbose_name = _('Gallery Options')
		verbose_name_plural = _('Galleries Options')

	def __str__(self):
		return self.title


class GalleyImages(BaseDescriptionImageModel):
	author = models.CharField(max_length=160, blank='true', verbose_name='Author')
	gallery_options = models.ForeignKey(GalleryOptions, verbose_name='Gallery Options')

	class Meta:
		verbose_name = _('Carousel')
		verbose_name_plural = _('Carousels')

	def __str__(self):
		return self.title


