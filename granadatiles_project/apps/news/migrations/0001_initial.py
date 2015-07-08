# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.utils.methods


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(max_length=160, null=True, blank=True)),
                ('title_pr', models.CharField(max_length=160, null=True, blank=True)),
                ('file', models.FileField(verbose_name='File', upload_to=apps.utils.methods.model_directory_path)),
            ],
            options={
                'verbose_name': 'Catalog',
                'verbose_name_plural': 'Catalogs',
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(max_length=160, null=True, blank=True)),
                ('title_pr', models.CharField(max_length=160, null=True, blank=True)),
                ('image', models.ImageField(upload_to=apps.utils.methods.model_directory_path)),
                ('description', models.TextField()),
                ('description_es', models.TextField(null=True, blank=True)),
                ('description_pr', models.TextField(null=True, blank=True)),
                ('date', models.DateField(verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Magazine',
                'verbose_name_plural': 'Magazines',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(max_length=160, null=True, blank=True)),
                ('title_pr', models.CharField(max_length=160, null=True, blank=True)),
                ('url', models.CharField(max_length=11, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
    ]
