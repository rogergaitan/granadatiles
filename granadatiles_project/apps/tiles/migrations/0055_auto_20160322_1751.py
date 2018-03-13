# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0054_auto_20160322_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customizedtile',
            name='colors',
        ),
        migrations.AlterField(
            model_name='groupcolor',
            name='customized_tile',
            field=models.ForeignKey(related_name='color_groups', to='tiles.CustomizedTile'),
        ),
    ]
