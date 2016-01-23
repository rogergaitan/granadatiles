# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0005_auto_20160108_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customizedsampleorder',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Subtotal', null=True),
        ),
        migrations.AlterField(
            model_name='customizedtileorder',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Subtotal', null=True),
        ),
        migrations.AlterField(
            model_name='sampleorder',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Subtotal', null=True),
        ),
        migrations.AlterField(
            model_name='tileorder',
            name='subtotal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Subtotal', null=True),
        ),
    ]
