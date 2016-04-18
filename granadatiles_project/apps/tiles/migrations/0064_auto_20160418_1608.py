# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0063_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='height',
            field=models.FloatField(default=40, verbose_name='Height'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='box',
            name='length',
            field=models.FloatField(default=40, verbose_name='Lenght'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='box',
            name='width',
            field=models.FloatField(default=40, verbose_name='Width'),
            preserve_default=False,
        ),
    ]
