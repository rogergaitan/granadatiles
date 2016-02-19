# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0003_galleryimage_tiles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryimage',
            name='galleryCategory',
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='gallery_categories',
            field=models.ManyToManyField(verbose_name='Gallery Categories', to='galleries.GalleryCategory', related_name='images'),
        ),
    ]
