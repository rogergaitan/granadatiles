# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0028_box'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='box',
            options={'verbose_name_plural': 'Boxes', 'verbose_name': 'Box'},
        ),
        migrations.AddField(
            model_name='tile',
            name='override_collection_box',
            field=models.BooleanField(default=False, verbose_name='Override Collection Box'),
        ),
    ]
