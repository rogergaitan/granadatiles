# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0023_auto_20160509_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectioncontent',
            name='page_title',
            field=models.CharField(null=True, max_length=500, verbose_name='Pagetitle', default='', blank=True),
        ),
        migrations.AddField(
            model_name='collectioncontent',
            name='page_title_es',
            field=models.CharField(null=True, max_length=500, verbose_name='Pagetitle_es', default='', blank=True),
        ),
        migrations.AddField(
            model_name='extendedflatpage',
            name='page_title',
            field=models.CharField(null=True, max_length=500, verbose_name='Pagetitle', default='', blank=True),
        ),
        migrations.AddField(
            model_name='extendedflatpage',
            name='page_title_es',
            field=models.CharField(null=True, max_length=500, verbose_name='Pagetitle_es', default='', blank=True),
        ),
    ]
