# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tiles', '0024_remove_tile_in_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('user', models.ForeignKey(verbose_name='Portfolio', to=settings.AUTH_USER_MODEL, related_name='portfolio')),
            ],
        ),
        migrations.AddField(
            model_name='tile',
            name='customized',
            field=models.BooleanField(verbose_name='Customized', default=False),
        ),
        migrations.AddField(
            model_name='tile',
            name='portfolio',
            field=models.ForeignKey(verbose_name='Portfolio', to='tiles.Portfolio', blank=True, related_name='tiles', null=True),
        ),
    ]
