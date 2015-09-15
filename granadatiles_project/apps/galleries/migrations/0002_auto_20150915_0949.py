# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallerycategory',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
