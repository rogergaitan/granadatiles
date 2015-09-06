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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, blank=True, null=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, null=True)),
                ('url', models.CharField(max_length=200, blank=True, null=True, verbose_name='Link')),
                ('date', models.DateField(verbose_name='Date')),
                ('cover', sorl.thumbnail.fields.ImageField(upload_to='Magazines')),
            ],
            options={
                'verbose_name_plural': 'Articles',
                'verbose_name': 'Article',
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(max_length=150, blank=True, null=True, verbose_name='Name')),
                ('file', models.FileField(upload_to='Catalogs', verbose_name='File')),
            ],
            options={
                'verbose_name_plural': 'Catalogs',
                'verbose_name': 'Catalog',
            },
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
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
            field=models.ForeignKey(to='news.Magazine', related_name='articles'),
        ),
    ]
