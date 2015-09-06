# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import apps.utils.methods


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0001_initial'),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, max_length=160, blank=True)),
                ('message', models.TextField()),
                ('message_es', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Manageable Areas',
                'verbose_name': 'Manageable Area',
            },
        ),
        migrations.CreateModel(
            name='CustomMessage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, max_length=160, blank=True)),
                ('description', models.TextField()),
                ('description_es', models.TextField(null=True, blank=True)),
                ('name', models.CharField(max_length=160)),
                ('name_es', models.CharField(null=True, max_length=160, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Messages',
                'ordering': ('name',),
                'verbose_name': 'Message',
            },
        ),
        migrations.CreateModel(
            name='FeaturedVideo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, max_length=160, blank=True)),
                ('video', models.URLField(null=True, max_length=11, verbose_name='Youtube Video ID', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Videos',
                'verbose_name': 'Video',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, max_length=160, blank=True)),
                ('description', models.TextField()),
                ('description_es', models.TextField(null=True, blank=True)),
                ('name', models.CharField(max_length=160)),
                ('name_es', models.CharField(null=True, max_length=160, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Sections',
                'ordering': ('name',),
                'verbose_name': 'Section',
            },
        ),
        migrations.CreateModel(
            name='SectionImage',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, max_length=160, blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=apps.utils.methods.model_directory_path)),
                ('target', models.BooleanField(default=False)),
                ('designer', models.CharField(null=True, max_length=200, verbose_name='Designer', blank=True)),
                ('photographer', models.CharField(null=True, max_length=200, verbose_name='Photographer', blank=True)),
                ('article', models.ManyToManyField(to='news.Article', related_name='Article')),
                ('section', models.ForeignKey(to='content.Section', related_name='Images')),
                ('tile', models.ForeignKey(to='tiles.Tile', related_name='Tile')),
            ],
            options={
                'verbose_name_plural': 'Images',
                'verbose_name': 'Image',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=160)),
                ('name_es', models.CharField(null=True, max_length=160, blank=True)),
                ('url', models.URLField(null=True, verbose_name='Link', blank=True)),
                ('order', models.PositiveIntegerField(unique=True, verbose_name='Order')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name_plural': 'Social Media',
                'ordering': ('order',),
                'verbose_name': 'Social',
            },
        ),
    ]
