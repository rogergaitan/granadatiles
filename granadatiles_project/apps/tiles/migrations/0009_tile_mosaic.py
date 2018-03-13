# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0008_auto_20151117_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='mosaic',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='mosaic', blank=True, verbose_name='Mosaic'),
        ),
    ]
