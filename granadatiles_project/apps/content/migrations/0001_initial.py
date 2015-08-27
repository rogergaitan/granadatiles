# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('description', models.TextField()),
                ('description_es', models.TextField(blank=True, null=True)),
                ('description_pr', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(verbose_name='File', upload_to='carousels')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(max_length=160, blank=True, null=True)),
                ('title_pr', models.CharField(max_length=160, blank=True, null=True)),
                ('description', models.TextField()),
                ('description_es', models.TextField(blank=True, null=True)),
                ('description_pr', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=160)),
                ('name_es', models.CharField(max_length=160, blank=True, null=True)),
                ('name_pr', models.CharField(max_length=160, blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Seccion',
                'ordering': ('name',),
                'verbose_name_plural': 'Secciones',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=160)),
                ('name_es', models.CharField(max_length=160, blank=True, null=True)),
                ('name_pr', models.CharField(max_length=160, blank=True, null=True)),
                ('link', models.URLField(verbose_name='URL', null=True, blank=True)),
                ('order', models.PositiveIntegerField(verbose_name='Orden', unique=True)),
                ('active', models.BooleanField(verbose_name='Activo', default=True)),
            ],
            options={
                'verbose_name': 'Social',
                'ordering': ('order',),
                'verbose_name_plural': 'Social Media',
            },
        ),
        migrations.AddField(
            model_name='images',
            name='section',
            field=models.ForeignKey(related_name='carousel', to='content.Section'),
        ),
    ]
