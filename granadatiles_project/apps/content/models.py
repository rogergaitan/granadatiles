from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.flatpages.models import FlatPage
from core.models import BaseContentModel, BaseCatalogModel, BaseGalleryNavImageModel, BaseCatalogOrderModel, BaseSeoModel
from apps.news.models import Article
from apps.tiles.models import Tile, Collection
from apps.galleries.models import Designer, Photographer
from sorl.thumbnail.fields import ImageField


class Section(BaseCatalogModel, BaseContentModel, BaseSeoModel):
    
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
        ordering = ['order']


class Area(BaseContentModel):

    class Meta:
        verbose_name = _('Manageable Area')
        verbose_name_plural = _('Manageable Areas')
        ordering = ['title']


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
        ordering = ['title']


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
        ordering = ['title']
        

class ExtendedFlatPage(FlatPage, BaseSeoModel):
    MENU_CHOICES = (
            (1, 'Product Information'),
            (2, 'News/Press'),
            (3, 'About Us'),
        )
    url_es = models.CharField(_('URL_ES'), max_length=100, db_index=True, null=True, blank=True)
    title_es = models.CharField(max_length=200, blank=True, null = True)
    content_es = models.TextField(blank=True, null = True)
    menu_title = models.CharField(max_length=200, default='')
    menu_title_es = models.CharField(max_length=200, default='', blank=True)
    order = models.PositiveIntegerField(verbose_name=_('Order'),
                                        help_text='El orden en el que aparecera en el menu selecciondado despues de los elementos predefinidos')
    menu = models.IntegerField(choices=MENU_CHOICES, default=1)
    cover = ImageField(null=True, blank=True, verbose_name=_('Cover'))
    objects = models.Manager()

    class Meta:
        verbose_name = _('flat page')
        verbose_name_plural = _('flat pages')
        ordering = ('order', )

    def get_title(self, language):
        if language == 'es' and self.title_es is not None and self.title_es:
            return self.title_es
        return self.title

    def get_menu(self, language):
        if language == 'es' and self.menu_title_es is not None and self.menu_title_es:
            return self.menu_title_es
        return self.menu_title

    def get_content(self, language):
        if language == 'es' and self.content_es is not None and self.content_es:
            return self.content_es
        return self.content
    
    def get_url(self, language):
        if language == 'es' and self.url_es is not None and self.url_es:
            return self.url_es
        return self.url

    def __str__(self):
        return self.title

class CollectionContent(FlatPage, BaseSeoModel):
    url_es = models.CharField(_('URL_ES'), max_length=100, db_index=True, null=True, blank=True)
    title_es = models.CharField(max_length=200, blank=True, null = True)
    content_es = models.TextField(blank=True, null = True)
    menu_title = models.CharField(max_length=200, default='')
    menu_title_es = models.CharField(max_length=200, default='', blank=True)
    order = models.PositiveIntegerField(verbose_name=_('Order'),
                                        help_text='El orden en el que aparecera en el menu selecciondado despues de los elementos predefinidos')
    cover = ImageField(null=True, blank=True, verbose_name=_('Cover'))
    collection = models.ForeignKey(Collection, related_name='content', verbose_name='collection')
    objects = models.Manager()

    class Meta:
        verbose_name = _('Collection content')
        verbose_name_plural = _('Collection content')
        ordering = ('order', )

    def get_title(self, language):
        if language == 'es' and self.title_es is not None and self.title_es:
            return self.title_es
        return self.title

    def get_menu(self, language):
        if language == 'es' and self.menu_title_es is not None and self.menu_title_es:
            return self.menu_title_es
        return self.menu_title

    def get_content(self, language):
        if language == 'es' and self.content_es is not None and self.content_es:
            return self.content_es
        return self.content
    
    def get_url(self, language):
        if language == 'es' and self.url_es is not None and self.url_es:
            return self.url_es
        return self.url

    def __str__(self):
        return self.title
