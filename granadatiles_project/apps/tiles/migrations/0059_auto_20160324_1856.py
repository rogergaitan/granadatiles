# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0058_auto_20160324_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='menu_title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='collection',
            name='menu_title_es',
            field=models.CharField(default='', max_length=200, blank=True),
        ),
    ]
