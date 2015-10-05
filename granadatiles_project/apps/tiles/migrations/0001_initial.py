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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, null=True, blank=True, verbose_name='Title_es')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(null=True, blank=True, verbose_name='Description_es')),
                ('slug', models.SlugField(max_length=20, unique=True)),
                ('slug_es', models.SlugField(max_length=20, unique=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=core.models.model_directory_path, verbose_name='Image')),
                ('menu_image', sorl.thumbnail.fields.ImageField(upload_to='Galleries/menu', null=True, blank=True)),
                ('featured', models.BooleanField(default=True, verbose_name='Featured')),
                ('show_in_menu', models.BooleanField(default=True, verbose_name='Show in menu')),
            ],
            options={
                'verbose_name_plural': 'Collections',
                'verbose_name': 'Collection',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, null=True, blank=True, verbose_name='Title_es')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(null=True, blank=True, verbose_name='Description_es')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=core.models.model_directory_path, verbose_name='Image')),
                ('collection', models.ForeignKey(verbose_name='Collection', to='tiles.Collection', related_name='groups')),
            ],
            options={
                'verbose_name_plural': 'Groups',
                'verbose_name': 'Group',
            },
        ),
        migrations.CreateModel(
            name='PalleteColor',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, null=True, blank=True, verbose_name='Name_es')),
                ('hexadecimalCode', models.CharField(max_length=20, verbose_name='Color')),
            ],
            options={
                'verbose_name_plural': 'Pallete Colors',
                'verbose_name': 'Pallete Color',
            },
        ),
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, null=True, blank=True, verbose_name='Name_es')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='tiles', null=True, blank=True, verbose_name='Image')),
                ('main', models.BooleanField(default=False, help_text='Is the main tile of the design', verbose_name='Main')),
                ('colors', models.ManyToManyField(verbose_name='Tiles Colors', related_name='tiles', to='tiles.PalleteColor')),
            ],
            options={
                'verbose_name_plural': 'Tiles',
                'verbose_name': 'Tile',
            },
        ),
        migrations.CreateModel(
            name='TileDesign',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, null=True, blank=True, verbose_name='Name_es')),
                ('group', models.ForeignKey(verbose_name='Tiles Group', to='tiles.Group', related_name='designs')),
            ],
            options={
                'verbose_name_plural': 'Tile Designs',
                'verbose_name': 'Tile Design',
            },
        ),
        migrations.CreateModel(
            name='TileSize',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('weight', models.CharField(max_length=10, verbose_name='Weight')),
                ('thickness', models.CharField(max_length=10, verbose_name='Thickness')),
            ],
            options={
                'verbose_name_plural': 'Sizes',
                'verbose_name': 'Size',
            },
        ),
        migrations.AddField(
            model_name='tile',
            name='design',
            field=models.ForeignKey(verbose_name='Design', to='tiles.TileDesign', related_name='tiles'),
        ),
        migrations.AddField(
            model_name='tile',
            name='similar_tiles',
            field=models.ManyToManyField(verbose_name='Similar Tiles', to='tiles.Tile'),
        ),
        migrations.AddField(
            model_name='tile',
            name='sizes',
            field=models.ManyToManyField(verbose_name='Tiles Sizes', related_name='tiles', to='tiles.TileSize'),
        ),
    ]
