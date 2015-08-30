# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=160)),
                ('name_es', models.CharField(null=True, blank=True, max_length=160)),
                ('name_pr', models.CharField(null=True, blank=True, max_length=160)),
                ('description', models.TextField()),
                ('description_es', models.TextField(null=True, blank=True)),
                ('description_pr', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Administrable Area',
                'verbose_name_plural': 'Administrable Areas',
            },
        ),
        migrations.CreateModel(
            name='CustomMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, blank=True, max_length=160)),
                ('title_pr', models.CharField(null=True, blank=True, max_length=160)),
                ('description', models.TextField()),
                ('description_es', models.TextField(null=True, blank=True)),
                ('description_pr', models.TextField(null=True, blank=True)),
                ('name', models.CharField(max_length=160)),
                ('name_es', models.CharField(null=True, blank=True, max_length=160)),
                ('name_pr', models.CharField(null=True, blank=True, max_length=160)),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='FeaturedVideo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, blank=True, max_length=160)),
                ('title_pr', models.CharField(null=True, blank=True, max_length=160)),
                ('video', models.URLField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('description_image', models.TextField()),
                ('description_image_es', models.TextField(null=True, blank=True)),
                ('description_image_pr', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(verbose_name='File', upload_to='carousels')),
                ('target', models.BooleanField(default=False)),
                ('link', models.URLField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Carousel',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, blank=True, max_length=160)),
                ('title_pr', models.CharField(null=True, blank=True, max_length=160)),
                ('description', models.TextField()),
                ('description_es', models.TextField(null=True, blank=True)),
                ('description_pr', models.TextField(null=True, blank=True)),
                ('name', models.CharField(max_length=160)),
                ('name_es', models.CharField(null=True, blank=True, max_length=160)),
                ('name_pr', models.CharField(null=True, blank=True, max_length=160)),
            ],
            options={
                'verbose_name': 'Seccion',
                'verbose_name_plural': 'Secciones',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=160)),
                ('name_es', models.CharField(null=True, blank=True, max_length=160)),
                ('name_pr', models.CharField(null=True, blank=True, max_length=160)),
                ('link', models.URLField(null=True, verbose_name='URL', blank=True)),
                ('order', models.PositiveIntegerField(verbose_name='Orden', unique=True)),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Social',
                'verbose_name_plural': 'Social Media',
                'ordering': ('order',),
            },
        ),
        migrations.AddField(
            model_name='images',
            name='section',
            field=models.ForeignKey(to='content.Section', related_name='carousel'),
        ),
    ]
