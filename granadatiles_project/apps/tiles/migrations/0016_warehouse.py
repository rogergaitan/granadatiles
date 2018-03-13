# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0015_tile_tearsheet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, blank=True, null=True, verbose_name='Name_es')),
                ('zipcode', models.BooleanField(verbose_name='Zipcode')),
                ('custom', models.BooleanField(verbose_name='Custom')),
                ('in_stock', models.BooleanField(verbose_name='In Stock')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
