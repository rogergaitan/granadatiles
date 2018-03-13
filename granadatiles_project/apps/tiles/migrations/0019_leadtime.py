# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0018_auto_20151203_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(verbose_name='Title', max_length=150)),
                ('title_es', models.CharField(null=True, verbose_name='Title_es', blank=True, max_length=160)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(null=True, verbose_name='Description_es', blank=True)),
            ],
            options={
                'verbose_name': 'Leadtimes',
            },
        ),
    ]
