# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0026_auto_20151209_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('square_ft', models.PositiveIntegerField(null=True, verbose_name='Square feet', blank=True)),
                ('quantity', models.PositiveIntegerField(null=True, verbose_name='Quantity', blank=True)),
                ('boxes', models.PositiveIntegerField(null=True, verbose_name='Tile Boxes', blank=True)),
                ('tiles', models.ManyToManyField(to='tiles.Tile', verbose_name='Cart', related_name='cart')),
            ],
            options={
                'verbose_name_plural': 'Carts',
                'verbose_name': 'Cart',
            },
        ),
    ]
