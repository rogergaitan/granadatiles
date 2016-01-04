# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0040_customizedtile_portfolio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customizedtile',
            name='user',
        ),
    ]
