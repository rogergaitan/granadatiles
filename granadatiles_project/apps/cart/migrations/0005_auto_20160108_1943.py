# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0041_remove_customizedtile_user'),
        ('cart', '0004_sampleorder_subtotal'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomizedSampleOrder',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity', blank=True, null=True)),
                ('subtotal', models.FloatField(verbose_name='Subtotal', blank=True, null=True)),
                ('cart', models.ForeignKey(verbose_name='Customized Sample Orders', related_name='customized_sample_orders', to='cart.Cart')),
                ('customized_tile', models.ForeignKey(verbose_name='Customized Tiles', to='tiles.CustomizedTile')),
            ],
            options={
                'verbose_name': 'Customized Sample Order',
                'verbose_name_plural': 'Customized Sample Orders',
            },
        ),
        migrations.CreateModel(
            name='CustomizedTileOrder',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('sq_ft', models.PositiveIntegerField(verbose_name='Square feet', blank=True, null=True)),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity', blank=True, null=True)),
                ('boxes', models.PositiveIntegerField(verbose_name='Tile Boxes', blank=True, null=True)),
                ('subtotal', models.FloatField(verbose_name='Subtotal', blank=True, null=True)),
                ('cart', models.ForeignKey(verbose_name='Customized Tile Orders', related_name='customized_tile_orders', to='cart.Cart')),
                ('customized_tile', models.ForeignKey(to='tiles.CustomizedTile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='sampleorder',
            old_name='tiles',
            new_name='tile',
        ),
        migrations.RenameField(
            model_name='tileorder',
            old_name='tiles',
            new_name='tile',
        ),
    ]
