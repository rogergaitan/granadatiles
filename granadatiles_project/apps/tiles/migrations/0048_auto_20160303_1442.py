# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0047_auto_20160301_2136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='palletecolor',
            options={'ordering': ['order'], 'verbose_name': 'Pallete Color', 'verbose_name_plural': 'Pallete Colors'},
        ),
        migrations.AddField(
            model_name='palletecolor',
            name='order',
            field=models.PositiveIntegerField(verbose_name='Order', default=1),
            preserve_default=False,
        ),
    ]
