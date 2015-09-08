# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='name_es',
            field=models.CharField(null=True, verbose_name='Name_es', blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='gallerycategory',
            name='name_es',
            field=models.CharField(null=True, verbose_name='Name_es', blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='description_es',
            field=models.TextField(null=True, verbose_name='Description_es', blank=True),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='title_es',
            field=models.CharField(null=True, verbose_name='Title_es', blank=True, max_length=160),
        ),
    ]
