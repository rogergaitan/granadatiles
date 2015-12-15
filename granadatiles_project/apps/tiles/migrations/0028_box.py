# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0027_auto_20151214_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('description', models.CharField(verbose_name='Description', max_length=100)),
                ('measurement_unit', models.PositiveIntegerField(choices=[(1, 'Unit'), (2, 'Square Foot')], verbose_name='Measurement Unit')),
                ('quantity', models.FloatField(verbose_name='Quantity')),
            ],
        ),
    ]
