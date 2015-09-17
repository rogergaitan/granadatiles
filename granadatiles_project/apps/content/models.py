from django.db import models
from apps.news.models import Article
from apps.tiles.models import Tile
from django.utils.translation import ugettext as _
from apps.galleries.models import Designer, Photographer
from core.models import BaseContentModel, BaseCatalogModel, BaseGallerieNavImageModel, BaseCatalogOrderModel


class Section(BaseCatalogModel, BaseContentModel):

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        ordering = ('name',)


class SectionImage(BaseGallerieNavImageModel):
    designer = models.ForeignKey(
        Designer, blank=True, null=True, related_name='covers',
        verbose_name=_('Author'))
    photographer = models.ForeignKey(
        Photographer, blank=True, null=True, related_name='covers',
        verbose_name=_('Photographer'))
    section = models.ForeignKey(Section, related_name='images')
    articles = models.ManyToManyField(Article)
    tile = models.ForeignKey(
        Tile, related_name='pictures', verbose_name=_('Tile'))

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')


class Social(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('Name'))
    url = models.URLField(blank=True, null=True, verbose_name=_('Link'))
    order = models.PositiveIntegerField(unique=True, verbose_name=_('Order'))
    active = models.BooleanField(default=True, verbose_name=_('Active'))
    css_class = models.CharField(max_length=30, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Social Media'
        ordering = ('order',)


class FeaturedVideo(BaseCatalogOrderModel):
    video = models.URLField(max_length=150, verbose_name=_('Video Url'))

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')


class Area(BaseContentModel):

    class Meta:
        verbose_name = _('Manageable Area')
        verbose_name_plural = _('Manageable Areas')


class Testimony(BaseContentModel):
    subtitle = models.CharField(max_length=150, verbose_name=_('Subtitle'))

    subtitle_es = models.CharField(max_length=150, verbose_name=_('Subtitle_es'))

    def get_subtitle(self, language=None):
        if language == 'es' and self.subtitle_es is not None and self.subtitle_es:
            return self.subtitle_es
        return self.subtitle

    class Meta:
        verbose_name = _('Testimony')
        verbose_name_plural = _('Testimonials')
