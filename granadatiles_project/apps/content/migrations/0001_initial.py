# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
        ('tiles', '0001_initial'),
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, blank=True, null=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Manageable Areas',
                'verbose_name': 'Manageable Area',
            },
        ),
        migrations.CreateModel(
            name='FeaturedVideo',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, blank=True, null=True, verbose_name='Name')),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, blank=True, null=True, verbose_name='Name')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, blank=True, null=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SectionImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, blank=True, null=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, null=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=core.models.model_directory_path, verbose_name='Image')),
                ('target', models.BooleanField(default=False, help_text='Open in new tab')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('articles', models.ManyToManyField(to='news.Article')),
                ('designer', models.ForeignKey(blank=True, related_name='covers', null=True, verbose_name='Author', to='galleries.Designer')),
                ('photographer', models.ForeignKey(blank=True, related_name='covers', null=True, verbose_name='Photographer', to='galleries.Photographer')),
                ('section', models.ForeignKey(to='content.Section', related_name='images')),
                ('tile', models.ForeignKey(related_name='pictures', verbose_name='Tile', to='tiles.Tile')),
            ],
            options={
                'verbose_name_plural': 'Images',
                'verbose_name': 'Image',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('order', models.PositiveIntegerField(unique=True, verbose_name='Order')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Social Media',
                'ordering': ('order',),
            },
        ),
    ]
