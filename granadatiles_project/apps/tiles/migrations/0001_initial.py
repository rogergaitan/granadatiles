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
            name='Collection',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, blank=True, null=True, verbose_name='Title_es')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, null=True, verbose_name='Description_es')),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('slug_es', models.SlugField(max_length=20, unique=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=core.models.model_directory_path, verbose_name='Image')),
                ('menu_image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='Galleries/menu', null=True)),
                ('featured', models.BooleanField(default=True, verbose_name='Featured')),
                ('show_in_menu', models.BooleanField(default=True, verbose_name='Show in menu')),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, blank=True, null=True, verbose_name='Title_es')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, null=True, verbose_name='Description_es')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=core.models.model_directory_path, verbose_name='Image')),
                ('collection', models.ForeignKey(to='tiles.Collection', related_name='groups', verbose_name='Collection')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='PalleteColor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, blank=True, null=True, verbose_name='Name_es')),
                ('hexadecimalCode', models.CharField(max_length=20, verbose_name='Color')),
            ],
            options={
                'verbose_name': 'Pallete Color',
                'verbose_name_plural': 'Pallete Colors',
            },
        ),
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, blank=True, null=True, verbose_name='Title_es')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, null=True, verbose_name='Description_es')),
                ('colors', models.ManyToManyField(to='tiles.PalleteColor', verbose_name='Tiles Colors', related_name='tiles')),
                ('group', models.ForeignKey(to='tiles.Group', related_name='tiles', verbose_name='Tiles Group')),
            ],
            options={
                'verbose_name': 'Tile',
                'verbose_name_plural': 'Tiles',
            },
        ),
        migrations.CreateModel(
            name='TileSize',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('weight', models.CharField(max_length=10, verbose_name='Weight')),
                ('thickness', models.CharField(max_length=10, verbose_name='Thickness')),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
            },
        ),
        migrations.AddField(
            model_name='tile',
            name='sizes',
            field=models.ManyToManyField(to='tiles.TileSize', verbose_name='Tiles Sizes', related_name='tiles'),
        ),
    ]
