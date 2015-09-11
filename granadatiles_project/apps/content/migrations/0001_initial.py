# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
        ('galleries', '0001_initial'),
        ('tiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(null=True, max_length=160, verbose_name='Title_es', blank=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(null=True, verbose_name='Description_es', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Manageable Areas',
                'verbose_name': 'Manageable Area',
            },
        ),
        migrations.CreateModel(
            name='FeaturedVideo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(null=True, max_length=150, verbose_name='Name_es', blank=True)),
                ('order', models.PositiveIntegerField(unique=True, verbose_name='Order')),
                ('video', models.URLField(max_length=150, verbose_name='Video Url')),
            ],
            options={
                'verbose_name_plural': 'Videos',
                'verbose_name': 'Video',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(null=True, max_length=150, verbose_name='Name_es', blank=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(null=True, max_length=160, verbose_name='Title_es', blank=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(null=True, verbose_name='Description_es', blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Sections',
                'verbose_name': 'Section',
            },
        ),
        migrations.CreateModel(
            name='SectionImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(null=True, max_length=160, verbose_name='Title_es', blank=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(null=True, verbose_name='Description_es', blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=core.models.model_directory_path, verbose_name='Image')),
                ('target', models.BooleanField(default=False, help_text='Open in new tab')),
                ('link', models.URLField(null=True, verbose_name='Link', blank=True)),
                ('articles', models.ManyToManyField(to='news.Article')),
                ('designer', models.ForeignKey(related_name='covers', to='galleries.Designer', blank=True, verbose_name='Author', null=True)),
                ('photographer', models.ForeignKey(related_name='covers', to='galleries.Photographer', blank=True, verbose_name='Photographer', null=True)),
                ('section', models.ForeignKey(related_name='images', to='content.Section')),
                ('tile', models.ForeignKey(related_name='pictures', to='tiles.Tile', verbose_name='Tile')),
            ],
            options={
                'verbose_name_plural': 'Images',
                'verbose_name': 'Image',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('url', models.URLField(null=True, verbose_name='Link', blank=True)),
                ('order', models.PositiveIntegerField(unique=True, verbose_name='Order')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'ordering': ('order',),
                'verbose_name_plural': 'Social Media',
                'verbose_name': 'Social',
            },
        ),
    ]
