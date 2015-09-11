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
            name='Collection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(null=True, max_length=160, verbose_name='Title_es', blank=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(null=True, verbose_name='Description_es', blank=True)),
                ('slug', models.SlugField(unique=True, max_length=20)),
                ('slug_es', models.SlugField(unique=True, max_length=20)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=core.models.model_directory_path, verbose_name='Image')),
            ],
            options={
                'verbose_name_plural': 'Collections',
                'verbose_name': 'Collection',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(null=True, max_length=160, verbose_name='Title_es', blank=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(null=True, verbose_name='Description_es', blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=core.models.model_directory_path, verbose_name='Image')),
                ('collection', models.ForeignKey(related_name='groups', to='tiles.Collection', verbose_name='Collection')),
            ],
            options={
                'verbose_name_plural': 'Groups',
                'verbose_name': 'Group',
            },
        ),
        migrations.CreateModel(
            name='PalleteColor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(null=True, max_length=150, verbose_name='Name_es', blank=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(null=True, max_length=160, verbose_name='Title_es', blank=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(null=True, verbose_name='Description_es', blank=True)),
                ('colors', models.ManyToManyField(related_name='tiles', to='tiles.PalleteColor', verbose_name='Tiles Colors')),
                ('group', models.ForeignKey(related_name='tiles', to='tiles.Group', verbose_name='Tiles Group')),
            ],
            options={
                'verbose_name_plural': 'Tiles',
                'verbose_name': 'Tile',
            },
        ),
        migrations.CreateModel(
            name='TileSize',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('weight', models.CharField(max_length=10, verbose_name='Weight')),
                ('thickness', models.CharField(max_length=10, verbose_name='Thickness')),
            ],
            options={
                'verbose_name_plural': 'Tile Sizes',
                'verbose_name': 'Tile Size',
            },
        ),
        migrations.AddField(
            model_name='tile',
            name='sizes',
            field=models.ManyToManyField(related_name='tiles', to='tiles.TileSize', verbose_name='Tiles Sizes'),
        ),
    ]
