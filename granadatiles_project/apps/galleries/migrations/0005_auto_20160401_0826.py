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
            options={'ordering': ['name'], 'verbose_name_plural': 'Designers', 'verbose_name': 'Designer'},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ['name'], 'verbose_name_plural': 'Galleries', 'verbose_name': 'Gallery'},
        ),
        migrations.AlterModelOptions(
            name='gallerycategory',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories', 'verbose_name': 'Category'},
        ),
        migrations.AlterModelOptions(
            name='galleryimage',
            options={'ordering': ['title'], 'verbose_name_plural': 'Images', 'verbose_name': 'Image'},
        ),
        migrations.AlterModelOptions(
            name='photographer',
            options={'ordering': ['name'], 'verbose_name_plural': 'Photographers', 'verbose_name': 'Photographer'},
        ),
    ]
