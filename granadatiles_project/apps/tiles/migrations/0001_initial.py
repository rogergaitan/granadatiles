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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=150)),
                ('title_es', models.CharField(blank=True, verbose_name='Title_es', null=True, max_length=160)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, verbose_name='Description_es', null=True)),
                ('slug', models.SlugField(unique=True, max_length=35)),
                ('slug_es', models.SlugField(unique=True, max_length=35)),
                ('image', sorl.thumbnail.fields.ImageField(verbose_name='Image', upload_to=core.models.model_directory_path)),
                ('menu_image', sorl.thumbnail.fields.ImageField(blank=True, upload_to='Galleries/menu', null=True)),
                ('featured', models.BooleanField(verbose_name='Featured', default=True)),
                ('show_in_menu', models.BooleanField(verbose_name='Show in menu', default=True)),
                ('introduction', models.TextField(verbose_name='Introduction')),
                ('introduction_es', models.TextField(blank=True, verbose_name='Introduction_es', null=True)),
            ],
            options={
                'verbose_name_plural': 'Collections',
                'verbose_name': 'Collection',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=150)),
                ('title_es', models.CharField(blank=True, verbose_name='Title_es', null=True, max_length=160)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, verbose_name='Description_es', null=True)),
                ('slug', models.SlugField(unique=True, max_length=35)),
                ('slug_es', models.SlugField(unique=True, max_length=35)),
                ('image', sorl.thumbnail.fields.ImageField(verbose_name='Image', upload_to=core.models.model_directory_path)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(blank=True, verbose_name='Name_es', null=True, max_length=150)),
                ('hexadecimalCode', models.CharField(verbose_name='Color', max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Pallete Colors',
                'verbose_name': 'Pallete Color',
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(blank=True, verbose_name='Name_es', null=True, max_length=150)),
                ('group', models.ForeignKey(verbose_name='Group', to='tiles.Group', related_name='styles')),
            ],
            options={
                'verbose_name_plural': 'Styles',
                'verbose_name': 'Style',
            },
        ),
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(blank=True, verbose_name='Name_es', null=True, max_length=150)),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, verbose_name='Image', null=True, upload_to='tiles')),
                ('main', models.BooleanField(verbose_name='Main', help_text='Is the main tile of the design', default=False)),
                ('colors', models.ManyToManyField(verbose_name='Tiles Colors', to='tiles.PalleteColor', related_name='tiles')),
            ],
            options={
                'verbose_name_plural': 'Tiles',
                'verbose_name': 'Tile',
            },
        ),
        migrations.CreateModel(
            name='TileDesign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(blank=True, verbose_name='Name_es', null=True, max_length=150)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.CharField(verbose_name='Weight', max_length=10)),
                ('thickness', models.CharField(verbose_name='Thickness', max_length=10)),
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
            field=models.ManyToManyField(verbose_name='Tiles Sizes', to='tiles.TileSize', related_name='tiles'),
        ),
    ]
