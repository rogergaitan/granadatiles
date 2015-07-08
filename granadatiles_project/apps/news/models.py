from apps.utils import BaseModel, BaseDescriptionImageModel
from apps.utils.methods import model_directory_path
from django.utils.translation import ugettext as _


class Catalog(BaseModel):
    file = FileField(upload_to=model_directory_path, verbose_name=_('File'))

    class Meta:
        verbose_name = _('Catalog')
        verbose_name_pluraal = _('Catalogs')

    def __str__(self):
        return self.title


class Magazine(BaseDescriptionImageModel):
    date = DateField(verbose_name=_('Date'))

    class Meta:
        verbose_name = _('Magazine')
        verbose_name_pluraal = _('Magazines')


    def __str__(self):
        return self.title


class Video(BaseModel):
    url = CharField(max_length=11, verbose_name=_('URL'))

    class Meta:
        verbose_name = _('Video')
        verbose_name_pluraal = _('Videos')

    def __str__(self):
        return self.title
