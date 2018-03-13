# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0056_tile_import_colors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tile',
            name='import_colors',
            field=models.CharField(help_text='Warning any input here will override the group colors!', null=True, max_length=50, blank=True, verbose_name='Import Colors'),
        ),
    ]
