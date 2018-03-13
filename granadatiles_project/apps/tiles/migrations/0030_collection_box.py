# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0029_auto_20151216_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='box',
            field=models.ForeignKey(null=True, to='tiles.Box', blank=True, verbose_name='Box'),
        ),
    ]
