# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='cover',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to=core.models.model_directory_path, default='image.png', verbose_name='Image'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='url',
            field=models.URLField(null=True, blank=True, verbose_name='Link'),
        ),
    ]
