# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0053_auto_20160322_1930'),
    ]

    operations = [
        migrations.CreateModel(
            name='TileGroupColor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('group', models.CharField(max_length=5)),
                ('color', models.ForeignKey(to='tiles.PalleteColor')),
            ],
        ),
        migrations.RemoveField(
            model_name='tile',
            name='colors',
        ),
        migrations.AddField(
            model_name='tilegroupcolor',
            name='tile',
            field=models.ForeignKey(to='tiles.Tile', related_name='colors'),
        ),
    ]
