# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0004_remove_tile_section_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='TileSize',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('weight', models.IntegerField()),
                ('thickness', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='tile',
            name='size',
            field=models.ManyToManyField(to='tiles.TileSize'),
        ),
    ]
