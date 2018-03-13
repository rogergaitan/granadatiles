# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0046_box_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='maximum_input_square_foot',
            field=models.PositiveIntegerField(verbose_name='Maximum Input Square Foot', default=5000),
        ),
        migrations.AlterField(
            model_name='collection',
            name='minimum_input_square_foot',
            field=models.PositiveIntegerField(verbose_name='Minimum Input Square Foot', default=1),
        ),
    ]
