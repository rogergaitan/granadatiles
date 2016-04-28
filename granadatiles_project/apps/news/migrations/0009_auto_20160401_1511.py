# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20160304_1013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalog',
            options={'verbose_name_plural': 'Catalogs', 'verbose_name': 'Catalog', 'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='magazine',
            options={'verbose_name_plural': 'Magazines', 'verbose_name': 'Magazine', 'ordering': ['name']},
        ),
    ]
