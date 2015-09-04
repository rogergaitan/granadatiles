# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.utils.methods


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=160)),
                ('name_es', models.CharField(blank=True, null=True, max_length=160)),
                ('logo', models.ImageField(upload_to=apps.utils.methods.model_directory_path)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(blank=True, null=True, max_length=160)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(blank=True, null=True, max_length=160)),
                ('image', models.ImageField(upload_to=apps.utils.methods.model_directory_path)),
                ('description', models.TextField()),
                ('description_es', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=160)),
                ('name_es', models.CharField(blank=True, null=True, max_length=160)),
                ('url', models.CharField(verbose_name='Link', blank=True, null=True, max_length=200)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(blank=True, null=True, max_length=160)),
                ('url', models.CharField(verbose_name='Youtube Video ID', max_length=11)),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='magazine',
            field=models.ForeignKey(related_name='Magazine', to='news.Magazine'),
        ),
    ]
