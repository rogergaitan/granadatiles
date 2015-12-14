# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0026_auto_20151209_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='maximum_input_square_foot',
            field=models.PositiveIntegerField(null=True, verbose_name='maximum_input_square_foot', blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='minimum_input_square_foot',
            field=models.PositiveIntegerField(null=True, verbose_name='minimum_input_square_foot', blank=True),
        ),
    ]
