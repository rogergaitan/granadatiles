# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0002_initial_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tilesize',
            options={'verbose_name': 'Size', 'verbose_name_plural': 'Sizes'},
        ),
    ]
