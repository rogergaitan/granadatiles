# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0022_auto_20151204_1444'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='in_stock',
            field=models.BooleanField(verbose_name='In stock', default=False),
        ),
    ]
