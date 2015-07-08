from django.db import models
from apps.utils.models import BaseModel, BaseDescriptionImageModel
from apps.utils.methods import model_directory_path
from django.utils.translation import ugettext as _


class Catalog(BaseModel):
    file = models.FileField(upload_to=model_directory_path, verbose_name=_('File'))

    class Meta:
        verbose_name = _('Catalog')
        verbose_name_plural = _('Catalogs')

    def __str__(self):
        return self.title


class Magazine(BaseDescriptionImageModel):
    date = models.DateField(verbose_name=_('Date'))

    class Meta:
        verbose_name = _('Magazine')
        verbose_name_plural = _('Magazines')

    def __str__(self):
        return self.title


class Video(BaseModel):
    url = models.CharField(max_length=11, verbose_name=_('Youtube Video ID'))

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')

    def __str__(self):
        return self.title

    def youtube_url_format(self):
        return 'https://www.youtube.com/watch?v={0}'.format(self.url)

    youtube_url_format.short_description = 'Youtube Video URL'
