# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0002_auto_20151111_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='is_sample',
            field=models.BooleanField(verbose_name='Is Sample', default=False),
        ),
        migrations.AddField(
            model_name='tile',
            name='new',
            field=models.BooleanField(max_length=10, verbose_name='New', default=False),
        ),
        migrations.AddField(
            model_name='tile',
            name='size',
            field=models.CharField(max_length=10, null=True, verbose_name='Size', default=''),
        ),
    ]
