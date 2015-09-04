# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.utils.methods


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
        ('content', '0003_initial_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(max_length=160, blank=True, null=True)),
                ('url', models.URLField(blank=True, verbose_name='Link', null=True)),
                ('logo', models.ImageField(upload_to=apps.utils.methods.model_directory_path)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='ImagesGroup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(max_length=160, blank=True, null=True)),
                ('image', models.ImageField(upload_to=apps.utils.methods.model_directory_path)),
                ('target', models.BooleanField(default=False)),
                ('url', models.URLField(blank=True, verbose_name='Link', null=True)),
                ('designer', models.CharField(max_length=200, blank=True, verbose_name='Designer', null=True)),
                ('photographer', models.CharField(max_length=200, blank=True, verbose_name='Photographer', null=True)),
                ('article', models.ManyToManyField(to='content.Article', related_name='Articles')),
                ('magazine', models.ManyToManyField(to='news.Magazine', related_name='Magazine')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.RemoveField(
            model_name='images',
            name='section',
        ),
        migrations.AlterModelOptions(
            name='area',
            options={'verbose_name': 'Manageable Area', 'verbose_name_plural': 'Manageable Areas'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ('name',), 'verbose_name': 'Section', 'verbose_name_plural': 'Sections'},
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
            field=models.URLField(blank=True, verbose_name='Link', null=True),
        ),
        migrations.AlterField(
            model_name='featuredvideo',
            name='video',
            field=models.URLField(max_length=11, blank=True, verbose_name='Youtube Video ID', null=True),
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
    ]
