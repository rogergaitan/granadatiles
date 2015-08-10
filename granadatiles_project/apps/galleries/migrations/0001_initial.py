# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.utils.methods


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(max_length=160, blank=True, null=True)),
                ('title_pr', models.CharField(max_length=160, blank=True, null=True)),
                ('image', models.ImageField(upload_to=apps.utils.methods.model_directory_path)),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.CreateModel(
            name='GalleryOptions',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(max_length=160, blank=True, null=True)),
                ('title_pr', models.CharField(max_length=160, blank=True, null=True)),
                ('gallery', models.ForeignKey(verbose_name='Gallery', to='galleries.Gallery')),
            ],
            options={
                'verbose_name': 'Gallery Options',
                'verbose_name_plural': 'Galleries Options',
            },
        ),
        migrations.CreateModel(
            name='GalleyImages',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(max_length=160, blank=True, null=True)),
                ('title_pr', models.CharField(max_length=160, blank=True, null=True)),
                ('image', models.ImageField(upload_to=apps.utils.methods.model_directory_path)),
                ('description', models.TextField()),
                ('description_es', models.TextField(blank=True, null=True)),
                ('description_pr', models.TextField(blank=True, null=True)),
                ('author', models.CharField(max_length=160, verbose_name='Author', blank='true')),
                ('gallery_options', models.ForeignKey(verbose_name='Gallery Options', to='galleries.GalleryOptions')),
            ],
            options={
                'verbose_name': 'Carousel',
                'verbose_name_plural': 'Carousels',
            },
        ),
    ]
