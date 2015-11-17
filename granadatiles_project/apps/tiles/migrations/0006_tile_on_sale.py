# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0005_auto_20151116_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='on_sale',
            field=models.BooleanField(default=False, verbose_name='On Sale'),
        ),
    ]
