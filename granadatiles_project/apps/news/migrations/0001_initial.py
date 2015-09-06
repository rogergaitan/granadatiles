# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import apps.utils.methods


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=160)),
                ('name_es', models.CharField(null=True, max_length=160, blank=True)),
                ('logo', models.ImageField(upload_to=apps.utils.methods.model_directory_path)),
            ],
            options={
                'verbose_name_plural': 'Articles',
                'verbose_name': 'Article',
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, max_length=160, blank=True)),
                ('file', models.FileField(upload_to=apps.utils.methods.model_directory_path, verbose_name='File')),
            ],
            options={
                'verbose_name_plural': 'Catalogs',
                'verbose_name': 'Catalog',
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, max_length=160, blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=apps.utils.methods.model_directory_path)),
                ('description', models.TextField()),
                ('description_es', models.TextField(null=True, blank=True)),
                ('name', models.CharField(max_length=160)),
                ('name_es', models.CharField(null=True, max_length=160, blank=True)),
                ('url', models.CharField(null=True, max_length=200, verbose_name='Link', blank=True)),
                ('date', models.DateField(verbose_name='Date')),
            ],
            options={
                'verbose_name_plural': 'Magazines',
                'verbose_name': 'Magazine',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, max_length=160, blank=True)),
                ('url', models.CharField(max_length=11, verbose_name='Youtube Video ID')),
            ],
            options={
                'verbose_name_plural': 'Videos',
                'verbose_name': 'Video',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='magazine',
            field=models.ForeignKey(to='news.Magazine', related_name='Magazine'),
        ),
    ]
