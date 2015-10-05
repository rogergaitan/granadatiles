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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Designers',
                'verbose_name': 'Designer',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, null=True, blank=True, verbose_name='Name_es')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='Gallery')),
            ],
            options={
                'verbose_name_plural': 'Galleries',
                'verbose_name': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='GalleryCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, null=True, blank=True, verbose_name='Name_es')),
                ('gallery', models.ForeignKey(verbose_name='Gallery', to='galleries.Gallery', related_name='categories')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, null=True, blank=True, verbose_name='Title_es')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(null=True, blank=True, verbose_name='Description_es')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=core.models.model_directory_path, verbose_name='Image')),
                ('designer', models.ForeignKey(null=True, related_name='gallery_images', blank=True, to='galleries.Designer', verbose_name='Author')),
                ('galleryCategory', models.ForeignKey(verbose_name='Gallery Category', to='galleries.GalleryCategory', related_name='images')),
            ],
            options={
                'verbose_name_plural': 'Images',
                'verbose_name': 'Image',
            },
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
            ],
            options={
                'verbose_name_plural': 'Photographers',
                'verbose_name': 'Photographer',
            },
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='photographer',
            field=models.ForeignKey(null=True, related_name='gallery_images', blank=True, to='galleries.Photographer', verbose_name='Photographer'),
        ),
    ]
