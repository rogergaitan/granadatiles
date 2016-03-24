# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0052_remove_customgroup_list_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customgroup',
            name='designs',
            field=models.ManyToManyField(related_name='custom_groups', to='tiles.TileDesign', verbose_name='Designs'),
        ),
    ]
