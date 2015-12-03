# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0020_lead_time_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leadtime',
            options={'verbose_name': 'Lead Times'},
        ),
        migrations.AddField(
            model_name='tile',
            name='in_stock',
            field=models.BooleanField(verbose_name='In Stock', default=''),
            preserve_default=False,
        ),
    ]
