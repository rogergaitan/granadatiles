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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(verbose_name='Name_es', max_length=150, blank=True, null=True)),
                ('collection', models.ForeignKey(related_name='uses', verbose_name='Collection', to='tiles.Collection')),
            ],
            options={
                'verbose_name': 'Use',
                'verbose_name_plural': 'Uses',
            },
        ),
    ]
