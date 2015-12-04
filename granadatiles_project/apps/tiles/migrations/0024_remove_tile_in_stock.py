# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0023_tile_in_stock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tile',
            name='in_stock',
        ),
    ]
