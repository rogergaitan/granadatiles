# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [

        ('news', '0001_initial'),
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=150)),
                ('title_es', models.CharField(blank=True, verbose_name='Title_es', null=True, max_length=160)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, verbose_name='Description_es', null=True)),
            ],
            options={
                'verbose_name_plural': 'Manageable Areas',
                'verbose_name': 'Manageable Area',
            },
        ),
        migrations.CreateModel(
            name='FeaturedVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(blank=True, verbose_name='Name_es', null=True, max_length=150)),
                ('order', models.PositiveIntegerField(verbose_name='Order', unique=True)),
                ('video', models.URLField(verbose_name='Video Url', max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Videos',
                'verbose_name': 'Video',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(blank=True, verbose_name='Name_es', null=True, max_length=150)),
                ('title', models.CharField(verbose_name='Title', max_length=150)),
                ('title_es', models.CharField(blank=True, verbose_name='Title_es', null=True, max_length=160)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, verbose_name='Description_es', null=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='Covers')),
                ('articles', models.ManyToManyField(blank=True, to='news.Article')),
                ('designer', models.ForeignKey(verbose_name='Designer', null=True, to='galleries.Designer', related_name='covers', blank=True)),
                ('featured_article', models.ForeignKey(null=True, to='news.Article', related_name='featured_article', blank=True)),
                ('photographer', models.ForeignKey(verbose_name='Photographer', null=True, to='galleries.Photographer', related_name='covers', blank=True)),
                ('section', models.ForeignKey(to='content.Section', related_name='images')),
                ('tile', models.ForeignKey(verbose_name='Tile', null=True, to='tiles.Tile', related_name='pictures', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Images',
                'verbose_name': 'Image',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=30)),
                ('url', models.URLField(blank=True, verbose_name='Link', null=True)),
                ('order', models.PositiveIntegerField(verbose_name='Order', unique=True)),
                ('active', models.BooleanField(verbose_name='Active', default=True)),
                ('css_class', models.CharField(editable=False, max_length=30)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=150)),
                ('title_es', models.CharField(blank=True, verbose_name='Title_es', null=True, max_length=160)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, verbose_name='Description_es', null=True)),
                ('subtitle', models.CharField(verbose_name='Subtitle', max_length=150)),
                ('subtitle_es', models.CharField(verbose_name='Subtitle_es', max_length=150)),
            ],
            options={
                'verbose_name_plural': 'Testimonials',
                'verbose_name': 'Testimony',
            },
        ),
    ]
