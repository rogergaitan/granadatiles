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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(blank=True, null=True, max_length=160)),
                ('title_pr', models.CharField(blank=True, null=True, max_length=160)),
                ('description', models.TextField()),
                ('description_es', models.TextField(blank=True, null=True)),
                ('description_pr', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Area Administrable',
                'verbose_name_plural': 'Areas Administrables',
            },
        ),
        migrations.CreateModel(
            name='CustomMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(blank=True, null=True, max_length=160)),
                ('title_pr', models.CharField(blank=True, null=True, max_length=160)),
                ('description', models.TextField()),
                ('description_es', models.TextField(blank=True, null=True)),
                ('description_pr', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=160)),
                ('name_es', models.CharField(blank=True, null=True, max_length=160)),
                ('name_pr', models.CharField(blank=True, null=True, max_length=160)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
            },
        ),
        migrations.CreateModel(
            name='FeaturedVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(blank=True, null=True, max_length=160)),
                ('title_pr', models.CharField(blank=True, null=True, max_length=160)),
                ('video', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('description_image', models.TextField()),
                ('description_image_es', models.TextField(blank=True, null=True)),
                ('description_image_pr', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='carousels', verbose_name='File')),
                ('target', models.BooleanField(default=False)),
                ('link', models.URLField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Carousel',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(blank=True, null=True, max_length=160)),
                ('title_pr', models.CharField(blank=True, null=True, max_length=160)),
                ('description', models.TextField()),
                ('description_es', models.TextField(blank=True, null=True)),
                ('description_pr', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=160)),
                ('name_es', models.CharField(blank=True, null=True, max_length=160)),
                ('name_pr', models.CharField(blank=True, null=True, max_length=160)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Seccion',
                'verbose_name_plural': 'Secciones',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=160)),
                ('name_es', models.CharField(blank=True, null=True, max_length=160)),
                ('name_pr', models.CharField(blank=True, null=True, max_length=160)),
                ('link', models.URLField(blank=True, verbose_name='URL', null=True)),
                ('order', models.PositiveIntegerField(verbose_name='Orden', unique=True)),
                ('active', models.BooleanField(verbose_name='Activo', default=True)),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'Social',
                'verbose_name_plural': 'Social Media',
            },
        ),
        migrations.AddField(
            model_name='images',
            name='section',
            field=models.ForeignKey(related_name='carousel', to='content.Section'),
        ),
    ]
