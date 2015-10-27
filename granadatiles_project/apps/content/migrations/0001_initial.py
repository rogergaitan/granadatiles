# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0001_initial'),
        ('news', '0002_initial_data'),
        ('galleries', '0002_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=150)),
                ('title_es', models.CharField(blank=True, verbose_name='Title_es', max_length=160, null=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, verbose_name='Description_es', null=True)),
            ],
            options={
                'verbose_name': 'Manageable Area',
                'verbose_name_plural': 'Manageable Areas',
            },
        ),
        migrations.CreateModel(
            name='FeaturedVideo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(blank=True, verbose_name='Name_es', max_length=150, null=True)),
                ('order', models.PositiveIntegerField(verbose_name='Order', unique=True)),
                ('video', models.URLField(verbose_name='Video Url', max_length=150)),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(blank=True, verbose_name='Name_es', max_length=150, null=True)),
                ('title', models.CharField(verbose_name='Title', max_length=150)),
                ('title_es', models.CharField(blank=True, verbose_name='Title_es', max_length=160, null=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, verbose_name='Description_es', null=True)),
            ],
            options={
                'verbose_name': 'Section',
                'ordering': ('name',),
                'verbose_name_plural': 'Sections',
            },
        ),
        migrations.CreateModel(
            name='SectionImage',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('image', models.ImageField(upload_to='Covers')),
                ('articles', models.ManyToManyField(blank=True, to='news.Article')),
                ('designer', models.ForeignKey(blank=True, related_name='covers', null=True, verbose_name='Designer', to='galleries.Designer')),
                ('featured_article', models.ForeignKey(blank=True, related_name='featured_article', null=True, to='news.Article')),
                ('photographer', models.ForeignKey(blank=True, related_name='covers', null=True, verbose_name='Photographer', to='galleries.Photographer')),
                ('section', models.ForeignKey(related_name='images', to='content.Section')),
                ('tile', models.ForeignKey(blank=True, related_name='pictures', null=True, verbose_name='Tile', to='tiles.Tile')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=30)),
                ('url', models.URLField(blank=True, verbose_name='Link', null=True)),
                ('order', models.PositiveIntegerField(verbose_name='Order', unique=True)),
                ('active', models.BooleanField(verbose_name='Active', default=True)),
                ('css_class', models.CharField(max_length=30, editable=False)),
            ],
            options={
                'verbose_name': 'Social',
                'ordering': ('order',),
                'verbose_name_plural': 'Social Media',
            },
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=150)),
                ('title_es', models.CharField(blank=True, verbose_name='Title_es', max_length=160, null=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, verbose_name='Description_es', null=True)),
                ('subtitle', models.CharField(verbose_name='Subtitle', max_length=150)),
                ('subtitle_es', models.CharField(verbose_name='Subtitle_es', max_length=150)),
            ],
            options={
                'verbose_name': 'Testimony',
                'verbose_name_plural': 'Testimonials',
            },
        ),
    ]
