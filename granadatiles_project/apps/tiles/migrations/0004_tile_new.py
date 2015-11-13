# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0003_tile_is_sample'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='new',
            field=models.BooleanField(default=False),
        ),
    ]
