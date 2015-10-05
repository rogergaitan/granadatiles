# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import core.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, null=True, blank=True, verbose_name='Title_es')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(null=True, blank=True, verbose_name='Description_es')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=core.models.model_directory_path, verbose_name='Image')),
                ('url', models.URLField(null=True, blank=True, verbose_name='Link')),
                ('date', models.DateField(verbose_name='Date')),
            ],
            options={
                'verbose_name_plural': 'Articles',
                'verbose_name': 'Article',
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, null=True, blank=True, verbose_name='Name_es')),
                ('file', models.FileField(upload_to='Catalogs', verbose_name='File')),
                ('image', models.ImageField(upload_to='Catalog', verbose_name='Image')),
            ],
            options={
                'verbose_name_plural': 'Catalogs',
                'verbose_name': 'Catalog',
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=130, verbose_name='Name')),
                ('logo', models.ImageField(upload_to='Magazines')),
            ],
            options={
                'verbose_name_plural': 'Magazines',
                'verbose_name': 'Magazine',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='magazine',
            field=models.ForeignKey(related_name='articles', to='news.Magazine'),
        ),
    ]
