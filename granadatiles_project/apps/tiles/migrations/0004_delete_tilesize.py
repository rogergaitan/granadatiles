# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0003_auto_20151113_2113'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TileSize',
        ),
    ]
