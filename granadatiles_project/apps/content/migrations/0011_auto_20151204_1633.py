# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0010_initial_index_navigation'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='meta_description',
            field=models.CharField(default='', verbose_name='Metadescription', max_length=500, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='section',
            name='meta_description_es',
            field=models.CharField(default='', verbose_name='Metadescription_es', max_length=500, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='section',
            name='meta_keywords',
            field=models.CharField(default='', verbose_name='Metakeywords', max_length=500, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='section',
            name='meta_keywords_es',
            field=models.CharField(default='', verbose_name='Metakeywords_es', max_length=500, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='section',
            name='page_title',
            field=models.CharField(default='', verbose_name='Pagetitle', max_length=500, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='section',
            name='page_title_es',
            field=models.CharField(default='', verbose_name='Pagetitle_es', max_length=500, blank=True, null=True),
        ),
    ]
