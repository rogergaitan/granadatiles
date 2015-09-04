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
            name='SectionImage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(blank=True, null=True, max_length=160)),
                ('image', models.ImageField(upload_to=apps.utils.methods.model_directory_path)),
                ('target', models.BooleanField(default=False)),
                ('url', models.URLField(verbose_name='Link', blank=True, null=True)),
                ('designer', models.CharField(verbose_name='Designer', blank=True, null=True, max_length=200)),
                ('photographer', models.CharField(verbose_name='Photographer', blank=True, null=True, max_length=200)),
                ('article', models.ManyToManyField(related_name='Article', to='news.Article')),
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
            field=models.URLField(verbose_name='Link', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='featuredvideo',
            name='video',
            field=models.URLField(verbose_name='Youtube Video ID', blank=True, null=True, max_length=11),
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
            model_name='sectionimage',
            name='section',
            field=models.ForeignKey(related_name='Images', to='content.Section'),
        ),
        migrations.AddField(
            model_name='sectionimage',
            name='tile',
            field=models.ForeignKey(related_name='Tile', to='tiles.Tile'),
        ),
    ]
