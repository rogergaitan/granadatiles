# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_auto_20150904_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectionimage',
            name='url',
        ),
    ]
