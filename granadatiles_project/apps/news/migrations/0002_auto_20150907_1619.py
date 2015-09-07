# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='description_es',
            field=models.TextField(null=True, verbose_name='Description_es', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title_es',
            field=models.CharField(null=True, verbose_name='Title_es', blank=True, max_length=160),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='name_es',
            field=models.CharField(null=True, verbose_name='Name_es', blank=True, max_length=150),
        ),
    ]
