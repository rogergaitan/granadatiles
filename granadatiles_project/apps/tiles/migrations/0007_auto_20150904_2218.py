# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0006_auto_20150904_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='PalleteColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=160)),
                ('name_es', models.CharField(null=True, blank=True, max_length=160)),
                ('number', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='tile',
            name='colors',
            field=models.ManyToManyField(to='tiles.PalleteColor'),
        ),
    ]
