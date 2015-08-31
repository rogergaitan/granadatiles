# _*_ encoding: utf-8 _*_

from django.db import models
from apps.utils.models import BaseModel, BaseSectionModel,BaseNameModel,BaseCarouselImage, BaseMessageNameModel


# Create your models here.

class Section(BaseSectionModel):

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Seccion'
		verbose_name_plural = 'Secciones'
		ordering = ('name',)


class Images(BaseCarouselImage):
	section = models.ForeignKey(Section, related_name='carousel')

	class Meta:
		verbose_name = 'Image'
		verbose_name_plural = 'Carousel'


class Social(BaseNameModel):
	link = models.URLField(blank=True, null=True, verbose_name='URL')
	order = models.PositiveIntegerField(unique=True, verbose_name='Orden')
	active = models.BooleanField(default=True, verbose_name='Activo')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Social'
		verbose_name_plural = 'Social Media'
		ordering = ('order',)


class FeaturedVideo(BaseModel):
	video = models.URLField(blank=True, null=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Video'
		verbose_name_plural = 'Videos'


class CustomMessage(BaseSectionModel):

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Message'
		verbose_name_plural = 'Messages'
		ordering = ('name',)


class Area(BaseMessageNameModel):

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Administrable Area'
		verbose_name_plural = 'Administrable Areas'




