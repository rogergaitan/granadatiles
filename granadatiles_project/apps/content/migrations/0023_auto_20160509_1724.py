# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0022_auto_20160509_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendedflatpage',
            name='meta_description',
            field=models.CharField(null=True, max_length=500, verbose_name='Metadescription', default='', blank=True),
        ),
        migrations.AddField(
            model_name='extendedflatpage',
            name='meta_description_es',
            field=models.CharField(null=True, max_length=500, verbose_name='Metadescription_es', default='', blank=True),
        ),
        migrations.AddField(
            model_name='extendedflatpage',
            name='meta_keywords',
            field=models.CharField(null=True, max_length=500, verbose_name='Metakeywords', default='', blank=True),
        ),
        migrations.AddField(
            model_name='extendedflatpage',
            name='meta_keywords_es',
            field=models.CharField(null=True, max_length=500, verbose_name='Metakeywords_es', default='', blank=True),
        ),
    ]
