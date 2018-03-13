# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0031_tile_box'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='qty_is_sq_ft',
            field=models.BooleanField(default=False, verbose_name='Quantity Square Foot'),
        ),
    ]
