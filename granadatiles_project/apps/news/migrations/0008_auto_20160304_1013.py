# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_auto_20160303_1832'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalogpage',
            options={'verbose_name': 'Catalog Page', 'verbose_name_plural': 'Catalog Pages', 'ordering': ['page_number']},
        ),
    ]
