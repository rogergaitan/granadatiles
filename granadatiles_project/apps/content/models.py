from django.db import models
from apps.news.models import Article
from apps.tiles.models import Tile
from django.utils.translation import ugettext as _
from apps.galleries.models import Designer, Photographer
from core.models import BaseContentModel, BaseCatalogModel, BaseGalleryNavImageModel, BaseCatalogOrderModel
from .managers import SectionManager


class Section(BaseCatalogModel, BaseContentModel):
    page_title = models.CharField(default='', blank=True, null=True, max_length=500, verbose_name=_('Pagetitle'))
    page_title_es = models.CharField(default='', blank=True, null=True, max_length=500, verbose_name=_('Pagetitle_es'))
    meta_description = models.CharField(default='', blank=True, null=True, max_length=500,
                                        verbose_name=_('Metadescription'))
    meta_description_es = models.CharField(default='', blank=True, null=True, max_length=500,
                                           verbose_name=_('Metadescription_es'))
    meta_keywords = models.CharField(default='', blank=True, null=True, max_length=500, verbose_name=_('Metakeywords'))
    meta_keywords_es = models.CharField(default='', blank=True, null=True, max_length=500,
                                        verbose_name=_('Metakeywords_es'))
    objects = models.Manager()
    seo = SectionManager()

    def get_page_title(self, language):
        if language == 'es' and self.page_title_es is not None and self.page_title_es:
            return self.page_title_es
        return self.page_title

    def get_meta_description(self, language):
        if language == 'es' and self.meta_description_es is not None and self.meta_description_es:
            return self.meta_description_es
        return self.meta_description

    def get_meta_keywords(self, language):
        if language == 'es' and self.meta_keywords_es is not None and self.meta_keywords_es:
            return self.meta_keywords_es
        return self.meta_keywords

    class Meta:
        verbose_name = _('Section')
        verbose_name_plural = _('Sections')
        ordering = ('name',)


class SectionImage(models.Model):
    image = models.ImageField(upload_to="Covers")
    designer = models.ForeignKey(
        Designer, blank=True, null=True, related_name='covers',
        verbose_name=_('Designer'))
    photographer = models.ForeignKey(
        Photographer, blank=True, null=True, related_name='covers',
        verbose_name=_('Photographer'))
    section = models.ForeignKey(Section, related_name='images')
    articles = models.ManyToManyField(Article,
                                        blank=True)
    featured_article = models.ForeignKey(Article, related_name='featured_article',
                                            null=True, blank=True)
    tile = models.ForeignKey(
        Tile, related_name='pictures', verbose_name=_('Tile'), null = True,
         blank = True)

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


class IndexNavigation(BaseGalleryNavImageModel):
    link_es = models.URLField(blank=True, null=True, verbose_name=_('Link_es'))
    action_name = models.CharField(max_length = 200 ,verbose_name=_('Action Name'))
    action_name_es = models.CharField(max_length = 200, blank= True, null = True, verbose_name=_('Action Name_es'))

    def get_link(self, language = None):
        if language == 'es' and self.link_es:
            return self.link_es
        return self.link

    def get_action_name(self, language = None):
        if language == 'es' and self.action_name_es:
            return self.action_name_es
        return self.action_name

    class Meta:
        verbose_name = _('Index Link')
        verbose_name_plural = _('Index Links')
