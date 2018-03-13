# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0049_auto_20160316_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tile',
            name='mosaic',
        ),
    ]
