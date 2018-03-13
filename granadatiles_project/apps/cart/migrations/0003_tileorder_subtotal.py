# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20151211_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='tileorder',
            name='subtotal',
            field=models.FloatField(verbose_name='Subtotal', blank=True, null=True),
        ),
    ]
