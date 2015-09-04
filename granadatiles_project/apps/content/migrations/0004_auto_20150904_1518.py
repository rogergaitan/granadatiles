# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.utils.methods


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0002_auto_20150904_1440'),
        ('news', '0001_initial'),
        ('content', '0003_initial_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, blank=True, max_length=160)),
                ('url', models.URLField(null=True, verbose_name='Link', blank=True)),
                ('logo', models.ImageField(upload_to=apps.utils.methods.model_directory_path)),
            ],
            options={
                'verbose_name_plural': 'Articles',
                'verbose_name': 'Article',
            },
        ),
        migrations.CreateModel(
            name='ImageGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, blank=True, max_length=160)),
                ('image', models.ImageField(upload_to=apps.utils.methods.model_directory_path)),
                ('target', models.BooleanField(default=False)),
                ('url', models.URLField(null=True, verbose_name='Link', blank=True)),
                ('designer', models.CharField(null=True, max_length=200, verbose_name='Designer', blank=True)),
                ('photographer', models.CharField(null=True, max_length=200, verbose_name='Photographer', blank=True)),
                ('article', models.ManyToManyField(related_name='Articles', to='content.Article')),
                ('magazine', models.ManyToManyField(related_name='Magazine', to='news.Magazine')),
            ],
            options={
                'verbose_name_plural': 'Images',
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
            options={'ordering': ('name',), 'verbose_name_plural': 'Sections', 'verbose_name': 'Section'},
        ),
        migrations.RemoveField(
            model_name='area',
            name='title_pr',
        ),
        migrations.RemoveField(
            model_name='custommessage',
            name='description_pr',
        ),
        migrations.RemoveField(
            model_name='custommessage',
            name='name_pr',
        ),
        migrations.RemoveField(
            model_name='custommessage',
            name='title_pr',
        ),
        migrations.RemoveField(
            model_name='featuredvideo',
            name='title_pr',
        ),
        migrations.RemoveField(
            model_name='section',
            name='description_pr',
        ),
        migrations.RemoveField(
            model_name='section',
            name='name_pr',
        ),
        migrations.RemoveField(
            model_name='section',
            name='title_pr',
        ),
        migrations.RemoveField(
            model_name='social',
            name='link',
        ),
        migrations.RemoveField(
            model_name='social',
            name='name_pr',
        ),
        migrations.AddField(
            model_name='social',
            name='url',
            field=models.URLField(null=True, verbose_name='Link', blank=True),
        ),
        migrations.AlterField(
            model_name='featuredvideo',
            name='video',
            field=models.URLField(null=True, max_length=11, verbose_name='Youtube Video ID', blank=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='active',
            field=models.BooleanField(verbose_name='Active', default=True),
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
            model_name='imagegroup',
            name='section',
            field=models.ForeignKey(to='content.Section', related_name='Images'),
        ),
        migrations.AddField(
            model_name='imagegroup',
            name='tile',
            field=models.ForeignKey(to='tiles.Tile', related_name='Tile'),
        ),
    ]
