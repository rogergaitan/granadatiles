# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0011_auto_20151120_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tile',
            name='colors',
            field=models.ManyToManyField(blank=True, verbose_name='Tiles Colors', to='tiles.PalleteColor', related_name='tiles'),
        ),
    ]
