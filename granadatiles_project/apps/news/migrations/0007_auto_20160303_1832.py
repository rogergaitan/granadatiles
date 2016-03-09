# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_catalog_page_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catalog',
            name='page_number',
        ),
        migrations.AddField(
            model_name='catalogpage',
            name='page_number',
            field=models.PositiveIntegerField(verbose_name='Page Number', default=1),
            preserve_default=False,
        ),
    ]
