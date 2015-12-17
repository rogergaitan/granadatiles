# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0032_tile_qty_is_sq_ft'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioTile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
            options={
                'verbose_name': 'Portfolio Tile',
                'verbose_name_plural': 'Portfolio Tiles',
            },
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name': 'Portfolios'},
        ),
        migrations.RemoveField(
            model_name='tile',
            name='portfolio',
        ),
        migrations.AddField(
            model_name='portfoliotile',
            name='portfolio',
            field=models.ForeignKey(to='tiles.Portfolio', verbose_name='Portfolio', related_name='tiles'),
        ),
        migrations.AddField(
            model_name='portfoliotile',
            name='tile',
            field=models.ForeignKey(to='tiles.Tile', verbose_name='Tile', related_name='portfolio'),
        ),
    ]
