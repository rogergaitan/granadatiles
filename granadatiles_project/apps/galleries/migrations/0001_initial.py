# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Designers',
                'verbose_name': 'Designer',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(blank=True, verbose_name='Name_es', null=True, max_length=150)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(blank=True, verbose_name='Name_es', null=True, max_length=150)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=150)),
                ('title_es', models.CharField(blank=True, verbose_name='Title_es', null=True, max_length=160)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, verbose_name='Description_es', null=True)),
                ('image', sorl.thumbnail.fields.ImageField(verbose_name='Image', upload_to=core.models.model_directory_path)),
                ('designer', models.ForeignKey(verbose_name='Author', null=True, to='galleries.Designer', related_name='gallery_images', blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Photographers',
                'verbose_name': 'Photographer',
            },
        ),
        migrations.AddField(
            model_name='galleryimage',
            name='photographer',
            field=models.ForeignKey(verbose_name='Photographer', null=True, to='galleries.Photographer', related_name='gallery_images', blank=True),
        ),
    ]
