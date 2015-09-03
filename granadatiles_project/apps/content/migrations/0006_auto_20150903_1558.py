# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20150903_1540'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagesgroup',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
    ]
