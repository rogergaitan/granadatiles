# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150807_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='title_pr',
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='description_pr',
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='title_pr',
        ),
        migrations.RemoveField(
            model_name='video',
            name='title_pr',
        ),
    ]
