# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0057_auto_20160324_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customgroup',
            name='designs',
        ),
        migrations.AddField(
            model_name='tiledesign',
            name='custom_groups',
            field=models.ManyToManyField(to='tiles.CustomGroup', verbose_name='Custom Groups', related_name='designs'),
        ),
    ]
