# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0045_auto_20160229_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='box',
            name='weight',
            field=models.PositiveIntegerField(verbose_name='Weight', default=0),
        ),
    ]
