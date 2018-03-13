# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_tileorder_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='sampleorder',
            name='subtotal',
            field=models.FloatField(null=True, blank=True, verbose_name='Subtotal'),
        ),
    ]
