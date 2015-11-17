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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(blank=True, max_length=150, verbose_name='Name_es', null=True)),
            ],
            options={
                'verbose_name_plural': 'Uses',
                'verbose_name': 'Use',
            },
        ),
        migrations.AddField(
            model_name='collection',
            name='uses',
            field=models.ManyToManyField(blank=True, related_name='collection', to='tiles.Use', verbose_name='Uses', null=True),
        ),
    ]
