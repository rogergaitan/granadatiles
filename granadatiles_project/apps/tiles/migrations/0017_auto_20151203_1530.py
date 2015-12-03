# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0016_warehouse'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='warehouse',
            options={'verbose_name': 'Warehouse', 'verbose_name_plural': 'Warehouse'},
        ),
        migrations.AddField(
            model_name='tile',
            name='custom',
            field=models.BooleanField(default=False, verbose_name='Custom'),
        ),
    ]
