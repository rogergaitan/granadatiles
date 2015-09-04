# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.utils.methods


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
        ('content', '0004_auto_20150904_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionImage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, blank=True, max_length=160)),
                ('image', models.ImageField(upload_to=apps.utils.methods.model_directory_path)),
                ('target', models.BooleanField(default=False)),
                ('url', models.URLField(null=True, blank=True, verbose_name='Link')),
                ('designer', models.CharField(null=True, blank=True, verbose_name='Designer', max_length=200)),
                ('photographer', models.CharField(null=True, blank=True, verbose_name='Photographer', max_length=200)),
                ('article', models.ManyToManyField(to='content.Article', related_name='Articles')),
                ('magazine', models.ManyToManyField(to='news.Magazine', related_name='Magazine')),
                ('section', models.ForeignKey(to='content.Section', related_name='Images')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.RemoveField(
            model_name='imagegroup',
            name='article',
        ),
        migrations.RemoveField(
            model_name='imagegroup',
            name='magazine',
        ),
        migrations.RemoveField(
            model_name='imagegroup',
            name='section',
        ),
        migrations.DeleteModel(
            name='ImageGroup',
        ),
    ]
