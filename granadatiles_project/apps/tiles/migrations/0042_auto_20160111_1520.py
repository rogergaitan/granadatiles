# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0041_remove_customizedtile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupcolor',
            name='customized_tile',
            field=models.ForeignKey(related_name='group_colors', to='tiles.CustomizedTile'),
        ),
        migrations.AlterField(
            model_name='warehouse',
            name='zipcode',
            field=models.CharField(max_length=5),
        ),
    ]
