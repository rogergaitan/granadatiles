# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0043_auto_20160201_2028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leadtime',
            options={'verbose_name_plural': 'Lead Times', 'verbose_name': 'Lead Time'},
        ),
        migrations.AlterField(
            model_name='palletecolor',
            name='hexadecimalCode',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=10),
        ),
        migrations.AlterField(
            model_name='tile',
            name='custom',
            field=models.BooleanField(verbose_name='In Stock', default=False),
        ),
    ]
