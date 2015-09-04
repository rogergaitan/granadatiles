# _*_ encoding: utf-8 _*_

from django.db import models
from apps.utils.models import BaseModel, BaseSectionModel, BaseNameModel, BaseImageModel, BaseMessageNameModel
from apps.news.models import Magazine
from django.utils.translation import ugettext as _
from apps.utils.methods import model_directory_path


# Create your models here.

class Section(BaseSectionModel):

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _('Section')
		verbose_name_plural = _('Sections')
		ordering = ('name',)


class Article(BaseModel):
	url = models.URLField(blank=True, null=True, verbose_name=_('Link'))
	logo = models.ImageField(upload_to=model_directory_path)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('Article')
		verbose_name_plural = _('Articles')


class SectionImage(BaseImageModel):
	target = models.BooleanField(default=False)
	url = models.URLField(blank=True, null=True, verbose_name=_('Link'))
	designer = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Designer'))
	photographer = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Photographer'))
	section = models.ForeignKey(Section, related_name=_('Images'))
	magazine = models.ManyToManyField(Magazine, related_name=_('Magazine'))
	article = models.ManyToManyField(Article, related_name=_('Articles'))

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = _('Image')
		verbose_name_plural = _('Images')


class Social(BaseNameModel):
	url = models.URLField(blank=True, null=True, verbose_name=_('Link'))
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




