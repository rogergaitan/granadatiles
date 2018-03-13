# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0037_tile_plane'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tile',
            name='plane',
            field=models.FileField(upload_to='designs', verbose_name='Plane', null=True, blank=True),
        ),
    ]
