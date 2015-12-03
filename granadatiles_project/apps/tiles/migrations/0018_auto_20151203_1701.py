# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0017_auto_20151203_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='warehouse',
            options={'verbose_name_plural': 'Warehouses', 'verbose_name': 'Warehouse'},
        ),
        migrations.AddField(
            model_name='group',
            name='show_in_web',
            field=models.BooleanField(verbose_name='Show in web', default=True),
        ),
        migrations.AddField(
            model_name='tiledesign',
            name='show_in_web',
            field=models.BooleanField(verbose_name='Show in web', default=True),
        ),
    ]
