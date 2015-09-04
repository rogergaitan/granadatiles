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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(max_length=160, null=True, blank=True)),
                ('url', models.URLField(verbose_name='Link', null=True, blank=True)),
                ('logo', models.ImageField(upload_to=apps.utils.methods.model_directory_path)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
        migrations.CreateModel(
            name='ImageGroup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(max_length=160, null=True, blank=True)),
                ('image', models.ImageField(upload_to=apps.utils.methods.model_directory_path)),
                ('target', models.BooleanField(default=False)),
                ('url', models.URLField(verbose_name='Link', null=True, blank=True)),
                ('designer', models.CharField(verbose_name='Designer', max_length=200, null=True, blank=True)),
                ('photographer', models.CharField(verbose_name='Photographer', max_length=200, null=True, blank=True)),
                ('article', models.ManyToManyField(related_name='Articles', to='content.Article')),
                ('magazine', models.ManyToManyField(related_name='Magazine', to='news.Magazine')),
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
            options={'verbose_name': 'Section', 'verbose_name_plural': 'Sections', 'ordering': ('name',)},
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
            field=models.URLField(verbose_name='Link', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='featuredvideo',
            name='video',
            field=models.URLField(verbose_name='Youtube Video ID', max_length=11, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='active',
            field=models.BooleanField(verbose_name='Active', default=True),
        ),
        migrations.AlterField(
            model_name='social',
            name='order',
            field=models.PositiveIntegerField(verbose_name='Order', unique=True),
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.AddField(
            model_name='imagegroup',
            name='section',
            field=models.ForeignKey(to='content.Section', related_name='Images'),
        ),
    ]
