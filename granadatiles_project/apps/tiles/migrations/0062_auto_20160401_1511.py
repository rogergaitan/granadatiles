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
            options={'verbose_name_plural': 'Collections', 'verbose_name': 'Collection', 'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name_plural': 'Groups', 'verbose_name': 'Group', 'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='leadtime',
            options={'verbose_name_plural': 'Lead Times', 'verbose_name': 'Lead Time', 'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='style',
            options={'verbose_name_plural': 'Styles', 'verbose_name': 'Style', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='tile',
            options={'verbose_name_plural': 'Tiles', 'verbose_name': 'Tile', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='tiledesign',
            options={'verbose_name_plural': 'Tile Designs', 'verbose_name': 'Tile Design', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='use',
            options={'verbose_name_plural': 'Uses', 'verbose_name': 'Use', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='warehouse',
            options={'verbose_name_plural': 'Warehouses', 'verbose_name': 'Warehouse', 'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='tile',
            name='width',
            field=models.IntegerField(blank=True, null=True, verbose_name='Width'),
        ),
    ]
