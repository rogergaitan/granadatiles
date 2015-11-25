# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0012_auto_20151125_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='featured',
            field=models.BooleanField(default=False, verbose_name='Featured'),
        ),
        migrations.AlterField(
            model_name='collection',
            name='show_in_menu',
            field=models.BooleanField(default=False, verbose_name='Show in menu'),
        ),
    ]
