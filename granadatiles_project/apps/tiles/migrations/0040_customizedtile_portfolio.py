# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0039_auto_20160104_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='customizedtile',
            name='portfolio',
            field=models.ForeignKey(to='tiles.Portfolio', default=1, related_name='customized_tiles'),
            preserve_default=False,
        ),
    ]
