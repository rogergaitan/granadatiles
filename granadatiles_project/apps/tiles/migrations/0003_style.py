# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0002_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Name', max_length=150)),
                ('name_es', models.CharField(null=True, verbose_name='Name_es', blank=True, max_length=150)),
                ('group', models.ForeignKey(to='tiles.Group', verbose_name='Group', related_name='styles')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
