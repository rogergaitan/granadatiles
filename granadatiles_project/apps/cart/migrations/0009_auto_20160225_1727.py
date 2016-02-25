# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customizedsampleorder',
            name='subtotal',
            field=models.DecimalField(null=True, max_digits=10, blank=True, verbose_name='Subtotal', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='customizedtileorder',
            name='subtotal',
            field=models.DecimalField(null=True, max_digits=10, blank=True, verbose_name='Subtotal', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='sampleorder',
            name='subtotal',
            field=models.DecimalField(null=True, max_digits=10, blank=True, verbose_name='Subtotal', decimal_places=2),
        ),
        migrations.AlterField(
            model_name='tileorder',
            name='subtotal',
            field=models.DecimalField(null=True, max_digits=10, blank=True, verbose_name='Subtotal', decimal_places=2),
        ),
    ]
