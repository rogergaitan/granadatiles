# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0068_auto_20160616_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tile',
            name='qty_is_sq_ft',
            field=models.BooleanField(default=False, verbose_name='Quantity is in Square Foot'),
        ),
    ]
