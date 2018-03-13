# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(verbose_name='Title', max_length=150)),
                ('title_es', models.CharField(blank=True, verbose_name='Title_es', null=True, max_length=160)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, verbose_name='Description_es', null=True)),
                ('image', sorl.thumbnail.fields.ImageField(verbose_name='Image', upload_to=core.models.model_directory_path)),
                ('url', models.URLField(blank=True, verbose_name='Link', null=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(blank=True, verbose_name='Name_es', null=True, max_length=150)),
                ('file', models.FileField(verbose_name='File', upload_to='Catalogs')),
                ('image', models.ImageField(verbose_name='Image', upload_to='Catalog')),
            ],
            options={
                'verbose_name_plural': 'Catalogs',
                'verbose_name': 'Catalog',
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='Name', max_length=130)),
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
            field=models.ForeignKey(to='news.Magazine', related_name='articles'),
        ),
    ]
