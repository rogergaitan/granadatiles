# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import apps.utils.methods


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, max_length=160, blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=apps.utils.methods.model_directory_path)),
            ],
            options={
                'verbose_name_plural': 'Galleries',
                'verbose_name': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='GalleryOptions',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, max_length=160, blank=True)),
                ('gallery', models.ForeignKey(to='galleries.Gallery', verbose_name='Gallery')),
            ],
            options={
                'verbose_name_plural': 'Galleries Options',
                'verbose_name': 'Gallery Options',
            },
        ),
        migrations.CreateModel(
            name='GalleyImages',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, max_length=160, blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=apps.utils.methods.model_directory_path)),
                ('description', models.TextField()),
                ('description_es', models.TextField(null=True, blank=True)),
                ('author', models.CharField(max_length=160, verbose_name='Author', blank='true')),
                ('gallery_options', models.ForeignKey(to='galleries.GalleryOptions', verbose_name='Gallery Options')),
            ],
            options={
                'verbose_name_plural': 'Carousels',
                'verbose_name': 'Carousel',
            },
        ),
    ]
