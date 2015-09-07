# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'verbose_name_plural': 'Collections', 'verbose_name': 'Collection'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name_plural': 'Groups', 'verbose_name': 'Group'},
        ),
        migrations.AlterModelOptions(
            name='palletecolor',
            options={'verbose_name_plural': 'Pallete Colors', 'verbose_name': 'Pallete Color'},
        ),
        migrations.AlterModelOptions(
            name='tile',
            options={'verbose_name_plural': 'Tiles', 'verbose_name': 'Tile'},
        ),
        migrations.AlterModelOptions(
            name='tilesize',
            options={'verbose_name_plural': 'Tile Sizes', 'verbose_name': 'Tile Size'},
        ),
        migrations.AlterField(
            model_name='group',
            name='collection',
            field=models.ForeignKey(related_name='groups', to='tiles.Collection', verbose_name='Collection'),
        ),
        migrations.AlterField(
            model_name='palletecolor',
            name='hexadecimalCode',
            field=models.CharField(max_length=20, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='tile',
            name='colors',
            field=models.ManyToManyField(verbose_name='Tiles Colors', related_name='tiles', to='tiles.PalleteColor'),
        ),
        migrations.AlterField(
            model_name='tile',
            name='group',
            field=models.ForeignKey(related_name='tiles', to='tiles.Group', verbose_name='Tiles Group'),
        ),
        migrations.AlterField(
            model_name='tile',
            name='sizes',
            field=models.ManyToManyField(verbose_name='Tiles Sizes', related_name='tiles', to='tiles.TileSize'),
        ),
        migrations.AlterField(
            model_name='tilesize',
            name='thickness',
            field=models.CharField(max_length=10, verbose_name='Thickness'),
        ),
        migrations.AlterField(
            model_name='tilesize',
            name='weight',
            field=models.CharField(max_length=10, verbose_name='Weight'),
        ),
    ]
