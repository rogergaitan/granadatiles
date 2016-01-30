# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20160122_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customizedsampleorder',
            name='subtotal',
            field=models.FloatField(blank=True, verbose_name='Subtotal', null=True),
        ),
        migrations.AlterField(
            model_name='customizedtileorder',
            name='subtotal',
            field=models.FloatField(blank=True, verbose_name='Subtotal', null=True),
        ),
        migrations.AlterField(
            model_name='sampleorder',
            name='subtotal',
            field=models.FloatField(blank=True, verbose_name='Subtotal', null=True),
        ),
        migrations.AlterField(
            model_name='tileorder',
            name='subtotal',
            field=models.FloatField(blank=True, verbose_name='Subtotal', null=True),
        ),
    ]
