# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0005_auto_20150904_2159'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tile',
            old_name='size',
            new_name='sizes',
        ),
    ]
