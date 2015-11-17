# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0004_delete_tilesize'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='thickness',
            field=models.CharField(null=True, default='', max_length=10, verbose_name='Thickness'),
        ),
        migrations.AddField(
            model_name='tile',
            name='weight',
            field=models.CharField(null=True, default='', max_length=10, verbose_name='Weight'),
        ),
    ]
