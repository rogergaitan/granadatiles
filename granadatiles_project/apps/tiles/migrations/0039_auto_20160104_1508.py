# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tiles', '0038_auto_20151228_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomizedTile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='GroupColor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('group', models.CharField(max_length=5)),
                ('color', models.ForeignKey(to='tiles.PalleteColor')),
                ('customized_tile', models.ForeignKey(to='tiles.CustomizedTile')),
            ],
        ),
        migrations.RemoveField(
            model_name='tile',
            name='customized',
        ),
        migrations.AddField(
            model_name='customizedtile',
            name='colors',
            field=models.ManyToManyField(to='tiles.PalleteColor', through='tiles.GroupColor'),
        ),
        migrations.AddField(
            model_name='customizedtile',
            name='tile',
            field=models.ForeignKey(to='tiles.Tile', related_name='customizations'),
        ),
        migrations.AddField(
            model_name='customizedtile',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='customizations'),
        ),
    ]
