# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, blank=True, null=True, verbose_name='Title_es')),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, null=True, verbose_name='Description_es')),
                ('url', models.CharField(max_length=200, blank=True, null=True, verbose_name='Link')),
                ('date', models.DateField(verbose_name='Date')),
                ('cover', sorl.thumbnail.fields.ImageField(upload_to='Magazines')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, blank=True, null=True, verbose_name='Name_es')),
                ('file', models.FileField(upload_to='Catalogs', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Catalog',
                'verbose_name_plural': 'Catalogs',
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=130, verbose_name='Name')),
                ('logo', models.ImageField(upload_to='Magazines')),
            ],
            options={
                'verbose_name': 'Magazine',
                'verbose_name_plural': 'Magazines',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='magazine',
            field=models.ForeignKey(to='news.Magazine', related_name='articles'),
        ),
    ]
