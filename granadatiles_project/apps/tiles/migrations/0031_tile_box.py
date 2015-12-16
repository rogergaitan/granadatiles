# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0030_collection_box'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='box',
            field=models.ForeignKey(blank=True, null=True, to='tiles.Box', verbose_name='Box'),
        ),
    ]
