# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0044_auto_20160225_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='maximum_input_square_foot',
            field=models.PositiveIntegerField(verbose_name='Maximum Input Square Foot', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='minimum_input_square_foot',
            field=models.PositiveIntegerField(verbose_name='Minimum Input Square Foot', blank=True, null=True),
        ),
    ]
