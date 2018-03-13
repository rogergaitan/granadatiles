# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0025_auto_20151204_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='height',
            field=models.IntegerField(verbose_name='Height', blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tile',
            name='width',
            field=models.IntegerField(verbose_name='Weight', blank=True, null=True),
        ),
    ]
