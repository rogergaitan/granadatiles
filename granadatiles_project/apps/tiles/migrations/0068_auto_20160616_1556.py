# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0067_auto_20160428_2307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customizedtile',
            options={'verbose_name_plural': 'Boxes', 'verbose_name': 'Box'},
        ),
        migrations.AlterField(
            model_name='tile',
            name='quantity_on_hand',
            field=models.FloatField(default=0, verbose_name='Quantity'),
        ),
    ]
