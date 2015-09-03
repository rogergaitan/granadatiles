# _*_ encoding: utf-8 _*_

from django.db import models
from apps.utils.models import BaseModel, BaseSectionModel, BaseNameModel, BaseImageModel, BaseMessageNameModel
from django.utils.translation import ugettext as _


# Create your models here.

class Section(BaseSectionModel):

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('Section')
		verbose_name_plural = _('Sections')
		ordering = ('name',)


class ImagesGroup(BaseImageModel):
	target = models.BooleanField(default=False)
	link = models.URLField(blank=True, null=True)
	designer = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Designer'))
	photographer = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Photographer'))
	section = models.ForeignKey(Section, related_name=_('Images'))

	class Meta:
		verbose_name = _('Image')
		verbose_name_plural = _('Images')


class Articles(BaseImageModel):
	imageGroup = models.ForeignKey(ImagesGroup, related_name=_('Articles'))

	class Meta:
		verbose_name = _('Article')
		verbose_name_plural = _('Articles')


class Social(BaseNameModel):
	link = models.URLField(blank=True, null=True, verbose_name='URL')
	order = models.PositiveIntegerField(unique=True, verbose_name=_('Order'))
	active = models.BooleanField(default=True, verbose_name=_('Active'))

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Social'
		verbose_name_plural = 'Social Media'
		ordering = ('order',)


class FeaturedVideo(BaseModel):
	video = models.URLField(blank=True, null=True, max_length=11, verbose_name=_('Youtube Video ID'))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('Video')
		verbose_name_plural = _('Videos')


class CustomMessage(BaseSectionModel):

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('Message')
		verbose_name_plural = _('Messages')
		ordering = ('name',)


class Area(BaseMessageNameModel):

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('Manageable Area')
		verbose_name_plural = _('Manageable Areas')




