# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0007_auto_20151117_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Use',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(verbose_name='Name_es', blank=True, null=True, max_length=150)),
            ],
            options={
                'verbose_name': 'Use',
                'verbose_name_plural': 'Uses',
            },
        ),
        migrations.AddField(
            model_name='collection',
            name='uses',
            field=models.ManyToManyField(verbose_name='Uses', blank=True, to='tiles.Use', related_name='collection'),
        ),
    ]
