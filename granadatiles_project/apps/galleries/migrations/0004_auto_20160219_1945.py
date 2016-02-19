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
            model_name='gallerycategory',
            name='images',
            field=models.ManyToManyField(related_name='categories', to='galleries.GalleryImage', verbose_name='Images'),
        ),
    ]
