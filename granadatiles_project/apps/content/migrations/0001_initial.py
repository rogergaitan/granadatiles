# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0001_initial'),
        ('galleries', '0001_initial'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, blank=True, null=True, verbose_name='Title_es')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, null=True, verbose_name='Description_es')),
            ],
            options={
                'verbose_name': 'Manageable Area',
                'verbose_name_plural': 'Manageable Areas',
            },
        ),
        migrations.CreateModel(
            name='FeaturedVideo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, blank=True, null=True, verbose_name='Name_es')),
                ('order', models.PositiveIntegerField(unique=True, verbose_name='Order')),
                ('video', models.URLField(max_length=150, verbose_name='Video Url')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, blank=True, null=True, verbose_name='Name_es')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, blank=True, null=True, verbose_name='Title_es')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, null=True, verbose_name='Description_es')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
            },
        ),
        migrations.CreateModel(
            name='SectionImage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, blank=True, null=True, verbose_name='Title_es')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, null=True, verbose_name='Description_es')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=core.models.model_directory_path, verbose_name='Image')),
                ('target', models.BooleanField(default=False, help_text='Open in new tab')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('articles', models.ManyToManyField(to='news.Article')),
                ('designer', models.ForeignKey(blank=True, to='galleries.Designer', null=True, related_name='covers', verbose_name='Author')),
                ('photographer', models.ForeignKey(blank=True, to='galleries.Photographer', null=True, related_name='covers', verbose_name='Photographer')),
                ('section', models.ForeignKey(to='content.Section', related_name='images')),
                ('tile', models.ForeignKey(to='tiles.Tile', related_name='pictures', verbose_name='Tile')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Link')),
                ('order', models.PositiveIntegerField(unique=True, verbose_name='Order')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('css_class', models.CharField(max_length=30, editable=False)),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'Social',
                'verbose_name_plural': 'Social Media',
            },
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, blank=True, null=True, verbose_name='Title_es')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, null=True, verbose_name='Description_es')),
                ('subtitle', models.CharField(max_length=150, verbose_name='Subtitle')),
                ('subtitle_es', models.CharField(max_length=150, verbose_name='Subtitle_es')),
            ],
            options={
                'verbose_name': 'Testimony',
                'verbose_name_plural': 'Testimonials',
            },
        ),
    ]
