# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0009_tile_mosaic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='style',
            name='group',
        ),
        migrations.AddField(
            model_name='style',
            name='design',
            field=models.ManyToManyField(to='tiles.TileDesign', related_name='styles', verbose_name='Designs'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='introduction',
            field=models.TextField(verbose_name='Introduction', default=''),
        ),
    ]
