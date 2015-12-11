# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0026_auto_20151209_1944'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('quantity', models.PositiveIntegerField(null=True, verbose_name='Quantity', blank=True)),
            ],
            options={
                'verbose_name': 'Sample Order',
                'verbose_name_plural': 'Sample Orders',
            },
        ),
        migrations.CreateModel(
            name='TileOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('sq_ft', models.PositiveIntegerField(null=True, verbose_name='Square feet', blank=True)),
                ('quantity', models.PositiveIntegerField(null=True, verbose_name='Quantity', blank=True)),
                ('boxes', models.PositiveIntegerField(null=True, verbose_name='Tile Boxes', blank=True)),
            ],
            options={
                'verbose_name': 'Tile Order',
                'verbose_name_plural': 'Tile Orders',
            },
        ),
        migrations.RemoveField(
            model_name='cart',
            name='boxes',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='square_ft',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='tiles',
        ),
        migrations.AddField(
            model_name='tileorder',
            name='cart',
            field=models.ForeignKey(related_name='tile_orders', verbose_name='Tile Orders', to='cart.Cart'),
        ),
        migrations.AddField(
            model_name='tileorder',
            name='tiles',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Tiles', to='tiles.Tile'),
        ),
        migrations.AddField(
            model_name='sampleorder',
            name='cart',
            field=models.ForeignKey(related_name='sample_orders', verbose_name='Sample Orders', to='cart.Cart'),
        ),
        migrations.AddField(
            model_name='sampleorder',
            name='tiles',
            field=models.ForeignKey(blank=True, null=True, verbose_name='Tiles', to='tiles.Tile'),
        ),
    ]
