# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0013_auto_20151125_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='style',
            name='design',
        ),
        migrations.AddField(
            model_name='tiledesign',
            name='styles',
            field=models.ManyToManyField(to='tiles.Style', verbose_name='Styles', related_name='designs'),
        ),
    ]
