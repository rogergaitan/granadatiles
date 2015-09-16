# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import core.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Designer',
                'verbose_name_plural': 'Designers',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, blank=True, null=True, verbose_name='Name_es')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='Gallery')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.CreateModel(
            name='GalleryCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, blank=True, null=True, verbose_name='Name_es')),
                ('gallery', models.ForeignKey(to='galleries.Gallery', related_name='categories', verbose_name='Gallery')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, blank=True, null=True, verbose_name='Title_es')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, null=True, verbose_name='Description_es')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=core.models.model_directory_path, verbose_name='Image')),
                ('designer', models.ForeignKey(blank=True, to='galleries.Designer', null=True, related_name='gallery_images', verbose_name='Author')),
                ('galleryCategory', models.ForeignKey(to='galleries.GalleryCategory', related_name='images', verbose_name='Gallery Category')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Photographer',
                'verbose_name_plural': 'Photographers',
            },
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='photographer',
            field=models.ForeignKey(blank=True, to='galleries.Photographer', null=True, related_name='gallery_images', verbose_name='Photographer'),
        ),
    ]
