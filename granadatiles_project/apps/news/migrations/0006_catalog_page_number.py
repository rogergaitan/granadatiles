# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_catalogpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='page_number',
            field=models.PositiveIntegerField(verbose_name='Page Number', default=1),
            preserve_default=False,
        ),
    ]
