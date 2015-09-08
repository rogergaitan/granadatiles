# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0002_auto_20150907_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='description_es',
            field=models.TextField(null=True, verbose_name='Description_es', blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='title_es',
            field=models.CharField(null=True, verbose_name='Title_es', blank=True, max_length=160),
        ),
        migrations.AlterField(
            model_name='group',
            name='description_es',
            field=models.TextField(null=True, verbose_name='Description_es', blank=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='title_es',
            field=models.CharField(null=True, verbose_name='Title_es', blank=True, max_length=160),
        ),
        migrations.AlterField(
            model_name='palletecolor',
            name='name_es',
            field=models.CharField(null=True, verbose_name='Name_es', blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='tile',
            name='description_es',
            field=models.TextField(null=True, verbose_name='Description_es', blank=True),
        ),
        migrations.AlterField(
            model_name='tile',
            name='title_es',
            field=models.CharField(null=True, verbose_name='Title_es', blank=True, max_length=160),
        ),
    ]
