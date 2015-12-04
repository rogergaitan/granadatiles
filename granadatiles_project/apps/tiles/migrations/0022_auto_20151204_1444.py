# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0021_auto_20151203_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tile',
            name='in_stock',
        ),
        migrations.AddField(
            model_name='tile',
            name='sample',
            field=models.ForeignKey(blank=True, related_name='samples', to='tiles.Tile', null=True, verbose_name='Sample'),
        ),
    ]
