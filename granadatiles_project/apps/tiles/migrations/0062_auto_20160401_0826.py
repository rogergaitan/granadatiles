# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0061_auto_20160329_2014'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['title'], 'verbose_name_plural': 'Collections', 'verbose_name': 'Collection'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['title'], 'verbose_name_plural': 'Groups', 'verbose_name': 'Group'},
        ),
        migrations.AlterModelOptions(
            name='leadtime',
            options={'ordering': ['title'], 'verbose_name_plural': 'Lead Times', 'verbose_name': 'Lead Time'},
        ),
        migrations.AlterModelOptions(
            name='style',
            options={'ordering': ['name'], 'verbose_name_plural': 'Styles', 'verbose_name': 'Style'},
        ),
        migrations.AlterModelOptions(
            name='tile',
            options={'ordering': ['name'], 'verbose_name_plural': 'Tiles', 'verbose_name': 'Tile'},
        ),
        migrations.AlterModelOptions(
            name='tiledesign',
            options={'ordering': ['name'], 'verbose_name_plural': 'Tile Designs', 'verbose_name': 'Tile Design'},
        ),
        migrations.AlterModelOptions(
            name='use',
            options={'ordering': ['name'], 'verbose_name_plural': 'Uses', 'verbose_name': 'Use'},
        ),
        migrations.AlterModelOptions(
            name='warehouse',
            options={'ordering': ['name'], 'verbose_name_plural': 'Warehouses', 'verbose_name': 'Warehouse'},
        ),
        migrations.AlterField(
            model_name='tile',
            name='width',
            field=models.IntegerField(blank=True, null=True, verbose_name='Width'),
        ),
    ]
