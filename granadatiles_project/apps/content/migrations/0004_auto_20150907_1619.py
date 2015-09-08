# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_initial_social'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='description_es',
            field=models.TextField(null=True, verbose_name='Description_es', blank=True),
        ),
        migrations.AlterField(
            model_name='area',
            name='title_es',
            field=models.CharField(null=True, verbose_name='Title_es', blank=True, max_length=160),
        ),
        migrations.AlterField(
            model_name='featuredvideo',
            name='name_es',
            field=models.CharField(null=True, verbose_name='Name_es', blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='section',
            name='description_es',
            field=models.TextField(null=True, verbose_name='Description_es', blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='name_es',
            field=models.CharField(null=True, verbose_name='Name_es', blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='section',
            name='title_es',
            field=models.CharField(null=True, verbose_name='Title_es', blank=True, max_length=160),
        ),
        migrations.AlterField(
            model_name='sectionimage',
            name='description_es',
            field=models.TextField(null=True, verbose_name='Description_es', blank=True),
        ),
        migrations.AlterField(
            model_name='sectionimage',
            name='title_es',
            field=models.CharField(null=True, verbose_name='Title_es', blank=True, max_length=160),
        ),
    ]
