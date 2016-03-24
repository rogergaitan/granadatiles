# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0050_remove_tile_mosaic'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(null=True, blank=True, max_length=160, verbose_name='Title_es')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(null=True, blank=True, verbose_name='Description_es')),
                ('slug', models.SlugField(unique=True, max_length=35)),
                ('slug_es', models.SlugField(null=True, unique=True, max_length=35)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=core.models.model_directory_path, verbose_name='Image')),
                ('list_id', models.CharField(unique=True, max_length=30, null=True, blank=True)),
                ('show_in_web', models.BooleanField(verbose_name='Show in web', default=True)),
                ('collection', models.ForeignKey(to='tiles.Collection', verbose_name='Collection', related_name='customgroups')),
                ('designs', models.ManyToManyField(to='tiles.TileDesign', related_name='designs', verbose_name='Designs')),
            ],
            options={
                'verbose_name_plural': 'Custom Groups',
                'verbose_name': 'Custom Group',
            },
        ),
    ]
