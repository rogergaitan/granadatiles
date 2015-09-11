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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(null=True, max_length=150, verbose_name='Name_es', blank=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(null=True, max_length=150, verbose_name='Name_es', blank=True)),
                ('gallery', models.ForeignKey(related_name='categories', to='galleries.Gallery', verbose_name='Gallery')),
            ],
            options={
                'verbose_name_plural': 'Galleries Categories',
                'verbose_name': 'Gallery Category',
            },
        ),
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(null=True, max_length=160, verbose_name='Title_es', blank=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(null=True, verbose_name='Description_es', blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=core.models.model_directory_path, verbose_name='Image')),
                ('designer', models.ForeignKey(related_name='gallery_images', to='galleries.Designer', blank=True, verbose_name='Author', null=True)),
                ('galleryCategory', models.ForeignKey(related_name='images', to='galleries.GalleryCategory', verbose_name='Gallery Category')),
            ],
            options={
                'verbose_name_plural': 'Images',
                'verbose_name': 'Image',
            },
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
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
            field=models.ForeignKey(related_name='gallery_images', to='galleries.Photographer', blank=True, verbose_name='Photographer', null=True),
        ),
    ]
