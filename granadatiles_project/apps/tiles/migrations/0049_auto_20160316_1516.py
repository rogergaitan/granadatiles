# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0048_auto_20160303_1442'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='palletecolor',
            options={'verbose_name': 'Palette Color', 'verbose_name_plural': 'Palette Colors', 'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='tile',
            name='rotate_deg1',
            field=models.PositiveIntegerField(default=0, choices=[(0, '0 deg'), (90, '90 deg'), (270, '270 deg'), (180, '180 deg')]),
        ),
        migrations.AddField(
            model_name='tile',
            name='rotate_deg2',
            field=models.PositiveIntegerField(default=90, choices=[(0, '0 deg'), (90, '90 deg'), (270, '270 deg'), (180, '180 deg')]),
        ),
        migrations.AddField(
            model_name='tile',
            name='rotate_deg3',
            field=models.PositiveIntegerField(default=270, choices=[(0, '0 deg'), (90, '90 deg'), (270, '270 deg'), (180, '180 deg')]),
        ),
        migrations.AddField(
            model_name='tile',
            name='rotate_deg4',
            field=models.PositiveIntegerField(default=180, choices=[(0, '0 deg'), (90, '90 deg'), (270, '270 deg'), (180, '180 deg')]),
        ),
    ]
