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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=150)),
                ('title_es', models.CharField(verbose_name='Title_es', null=True, blank=True, max_length=160)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(verbose_name='Description_es', null=True, blank=True)),
                ('slug', models.SlugField(max_length=35, unique=True)),
                ('slug_es', models.SlugField(max_length=35, unique=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=core.models.model_directory_path, verbose_name='Image')),
                ('menu_image', sorl.thumbnail.fields.ImageField(upload_to='Galleries/menu', null=True, blank=True)),
                ('featured', models.BooleanField(verbose_name='Featured', default=True)),
                ('show_in_menu', models.BooleanField(verbose_name='Show in menu', default=True)),
                ('introduction', models.TextField(verbose_name='Introduction')),
                ('introduction_es', models.TextField(verbose_name='Introduction_es', null=True, blank=True)),
                ('list_id', models.CharField(blank=True, unique=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name': 'Collection',
                'verbose_name_plural': 'Collections',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=150)),
                ('title_es', models.CharField(blank=True, verbose_name='Title_es', max_length=160, null=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, verbose_name='Description_es', null=True)),
                ('slug', models.SlugField(unique=True, max_length=35)),
                ('slug_es', models.SlugField(unique=True, max_length=35)),
                ('image', sorl.thumbnail.fields.ImageField(verbose_name='Image', upload_to=core.models.model_directory_path)),
                ('list_id', models.CharField(blank=True, unique=True, max_length=30, null=True)),
                ('collection', models.ForeignKey(related_name='groups', verbose_name='Collection', to='tiles.Collection')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='PalleteColor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(blank=True, verbose_name='Name_es', max_length=150, null=True)),
                ('hexadecimalCode', models.CharField(verbose_name='Color', max_length=20)),
            ],
            options={
                'verbose_name': 'Pallete Color',
                'verbose_name_plural': 'Pallete Colors',
            },
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(blank=True, verbose_name='Name_es', max_length=150, null=True)),
                ('group', models.ForeignKey(related_name='styles', verbose_name='Group', to='tiles.Group')),

            ],
            options={
                'verbose_name': 'Style',
                'verbose_name_plural': 'Styles',
            },
        ),
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(blank=True, verbose_name='Name_es', max_length=150, null=True)),
                ('list_id', models.CharField(blank=True, unique=True, max_length=30, null=True)),
                ('is_active', models.BooleanField(verbose_name='Is Active', default=True)),
                ('sales_price', models.FloatField(blank=True, verbose_name='Sales Price', null=True)),
                ('average_cost', models.FloatField(blank=True, verbose_name='Average Cost', null=True)),
                ('quantity_on_hand', models.IntegerField(verbose_name='Quantity', default=0)),
                ('sales_description', models.CharField(verbose_name='Sales description', max_length=450, default='')),
                ('sales_description_es', models.CharField(verbose_name='Sales description_es', max_length=450, default='')),
                ('image', sorl.thumbnail.fields.ImageField(blank=True, verbose_name='Image', upload_to='tiles', null=True)),
                ('main', models.BooleanField(verbose_name='Main', help_text='Is the main tile of the design', default=False)),
                ('colors', models.ManyToManyField(blank=True, verbose_name='Tiles Colors', related_name='tiles', to='tiles.PalleteColor')),
            ],
            options={
                'verbose_name': 'Tile',
                'verbose_name_plural': 'Tiles',
            },
        ),
        migrations.CreateModel(
            name='TileDesign',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(blank=True, verbose_name='Name_es', max_length=150, null=True)),
                ('group', models.ForeignKey(related_name='designs', verbose_name='Tiles Group', to='tiles.Group')),
            ],
            options={
                'verbose_name': 'Tile Design',
                'verbose_name_plural': 'Tile Designs',
            },
        ),
        migrations.CreateModel(
            name='TileSize',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('weight', models.CharField(verbose_name='Weight', max_length=10)),
                ('thickness', models.CharField(verbose_name='Thickness', max_length=10)),
            ],
            options={
                'verbose_name': 'Size',
                'verbose_name_plural': 'Sizes',
            },
        ),
        migrations.AddField(
            model_name='tile',
            name='design',
            field=models.ForeignKey(blank=True, related_name='tiles', null=True, verbose_name='Design', to='tiles.TileDesign'),
        ),
        migrations.AddField(
            model_name='tile',
            name='similar_tiles',
            field=models.ManyToManyField(blank=True, verbose_name='Similar Tiles', to='tiles.Tile'),
        ),
        migrations.AddField(
            model_name='tile',
            name='sizes',
            field=models.ManyToManyField(verbose_name='Tiles Sizes', related_name='tiles', to='tiles.TileSize'),
        ),
        migrations.AddField(
            model_name='style',
            name='design',
            field=models.ManyToManyField(blank=True, verbose_name='Tiles Sizes', related_name='tiles', to='tiles.TileSize'),
        ),
    ]
