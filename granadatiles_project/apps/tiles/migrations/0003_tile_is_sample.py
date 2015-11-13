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
            field=models.BooleanField(default=False),
        ),
    ]
