# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0004_auto_20160219_2112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='designer',
            options={'verbose_name_plural': 'Designers', 'verbose_name': 'Designer', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'Galleries', 'verbose_name': 'Gallery', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='gallerycategory',
            options={'verbose_name_plural': 'Categories', 'verbose_name': 'Category', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='galleryimage',
            options={'verbose_name_plural': 'Images', 'verbose_name': 'Image', 'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='photographer',
            options={'verbose_name_plural': 'Photographers', 'verbose_name': 'Photographer', 'ordering': ['name']},
        ),
    ]
