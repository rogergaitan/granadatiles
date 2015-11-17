# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0006_tile_on_sale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tile',
            name='colors',
        ),
        migrations.AddField(
            model_name='tile',
            name='colors',
            field=models.CharField(null=True, max_length=200, verbose_name='Colors'),
        ),
        migrations.DeleteModel(
            name='PalleteColor',
        ),
    ]
