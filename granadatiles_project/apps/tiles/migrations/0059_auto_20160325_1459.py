# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0058_auto_20160324_1447'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customgroup',
            options={'verbose_name_plural': 'Custom Groups', 'ordering': ['order'], 'verbose_name': 'Custom Group'},
        ),
        migrations.AddField(
            model_name='customgroup',
            name='order',
            field=models.PositiveIntegerField(verbose_name='Order', default=1),
            preserve_default=False,
        ),
    ]
