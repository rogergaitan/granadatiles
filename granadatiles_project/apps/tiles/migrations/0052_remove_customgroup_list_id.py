# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0051_customgroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customgroup',
            name='list_id',
        ),
    ]
