# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0021_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectioncontent',
            name='meta_description',
            field=models.CharField(default='', null=True, max_length=500, verbose_name='Metadescription', blank=True),
        ),
        migrations.AddField(
            model_name='collectioncontent',
            name='meta_description_es',
            field=models.CharField(default='', null=True, max_length=500, verbose_name='Metadescription_es', blank=True),
        ),
        migrations.AddField(
            model_name='collectioncontent',
            name='meta_keywords',
            field=models.CharField(default='', null=True, max_length=500, verbose_name='Metakeywords', blank=True),
        ),
        migrations.AddField(
            model_name='collectioncontent',
            name='meta_keywords_es',
            field=models.CharField(default='', null=True, max_length=500, verbose_name='Metakeywords_es', blank=True),
        ),
    ]
