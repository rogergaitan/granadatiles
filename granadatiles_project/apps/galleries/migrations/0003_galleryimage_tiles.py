# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0010_auto_20151118_1726'),
        ('galleries', '0002_initial_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='tiles',
            field=models.ManyToManyField(to='tiles.Tile', related_name='installation_photos', verbose_name='Tiles', blank=True),
        ),
    ]
