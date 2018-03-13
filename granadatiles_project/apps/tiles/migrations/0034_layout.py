# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0033_auto_20151217_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('length_ft', models.PositiveIntegerField(blank=True, null=True, verbose_name='Length Ft')),
                ('length_in', models.PositiveIntegerField(blank=True, null=True, verbose_name='Length In')),
                ('width_ft', models.PositiveIntegerField(blank=True, null=True, verbose_name='Width Ft')),
                ('width_in', models.PositiveIntegerField(blank=True, null=True, verbose_name='Width In')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Date')),
            ],
        ),
    ]
