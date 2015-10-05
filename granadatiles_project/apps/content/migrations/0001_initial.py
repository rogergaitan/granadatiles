# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, null=True, blank=True, verbose_name='Title_es')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(null=True, blank=True, verbose_name='Description_es')),
            ],
            options={
                'verbose_name_plural': 'Manageable Areas',
                'verbose_name': 'Manageable Area',
            },
        ),
        migrations.CreateModel(
            name='FeaturedVideo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, null=True, blank=True, verbose_name='Name_es')),
                ('order', models.PositiveIntegerField(verbose_name='Order', unique=True)),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, null=True, blank=True, verbose_name='Name_es')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, null=True, blank=True, verbose_name='Title_es')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(null=True, blank=True, verbose_name='Description_es')),
            ],
            options={
                'verbose_name_plural': 'Sections',
                'verbose_name': 'Section',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SectionImage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to='Covers')),
                ('articles', models.ManyToManyField(blank=True, to='news.Article')),
                ('designer', models.ForeignKey(null=True, related_name='covers', blank=True, to='galleries.Designer', verbose_name='Designer')),
                ('featured_article', models.ForeignKey(null=True, related_name='featured_article', blank=True, to='news.Article')),
                ('photographer', models.ForeignKey(null=True, related_name='covers', blank=True, to='galleries.Photographer', verbose_name='Photographer')),
                ('section', models.ForeignKey(related_name='images', to='content.Section')),
                ('tile', models.ForeignKey(null=True, related_name='pictures', blank=True, to='tiles.Tile', verbose_name='Tile')),
            ],
            options={
                'verbose_name_plural': 'Images',
                'verbose_name': 'Image',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('url', models.URLField(null=True, blank=True, verbose_name='Link')),
                ('order', models.PositiveIntegerField(verbose_name='Order', unique=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('css_class', models.CharField(max_length=30, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Social Media',
                'verbose_name': 'Social',
                'ordering': ('order',),
            },
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, null=True, blank=True, verbose_name='Title_es')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(null=True, blank=True, verbose_name='Description_es')),
                ('subtitle', models.CharField(max_length=150, verbose_name='Subtitle')),
                ('subtitle_es', models.CharField(max_length=150, verbose_name='Subtitle_es')),
            ],
            options={
                'verbose_name_plural': 'Testimonials',
                'verbose_name': 'Testimony',
            },
        ),
    ]
