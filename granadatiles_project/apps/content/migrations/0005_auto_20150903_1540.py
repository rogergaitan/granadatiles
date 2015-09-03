# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.utils.methods


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20150831_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(blank=True, null=True, max_length=160)),
                ('image', models.ImageField(upload_to=apps.utils.methods.model_directory_path)),
            ],
            options={
                'verbose_name_plural': 'Articles',
                'verbose_name': 'Article',
            },
        ),
        migrations.CreateModel(
            name='ImagesGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(blank=True, null=True, max_length=160)),
                ('image', models.ImageField(upload_to=apps.utils.methods.model_directory_path)),
                ('target', models.BooleanField(default=False)),
                ('link', models.URLField(blank=True, null=True)),
                ('designer', models.CharField(blank=True, null=True, max_length=200, verbose_name='Designer')),
                ('photographer', models.CharField(blank=True, null=True, max_length=200, verbose_name='Photographer')),
            ],
            options={
                'verbose_name_plural': 'Carousel',
                'verbose_name': 'Image',
            },
        ),
        migrations.RemoveField(
            model_name='images',
            name='section',
        ),
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name_plural': 'Manageable Areas', 'verbose_name': 'Manageable Area'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'verbose_name_plural': 'Sections', 'ordering': ('name',), 'verbose_name': 'Section'},
        ),
        migrations.RemoveField(
            model_name='custommessage',
            name='description_pr',
        ),
        migrations.RemoveField(
            model_name='section',
            name='description_pr',
        ),
        migrations.AlterField(
            model_name='featuredvideo',
            name='video',
            field=models.URLField(blank=True, null=True, max_length=11, verbose_name='Youtube Video ID'),
        ),
        migrations.AlterField(
            model_name='social',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
        migrations.AlterField(
            model_name='social',
            name='order',
            field=models.PositiveIntegerField(unique=True, verbose_name='Order'),
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.AddField(
            model_name='imagesgroup',
            name='section',
            field=models.ForeignKey(to='content.Section', related_name='Images'),
        ),
        migrations.AddField(
            model_name='articles',
            name='imageGroup',
            field=models.ForeignKey(to='content.ImagesGroup', related_name='Articles'),
        ),
    ]
