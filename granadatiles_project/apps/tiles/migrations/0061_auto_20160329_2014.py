# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0060_auto_20160325_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tile',
            name='import_colors',
            field=models.CharField(verbose_name='Import Colors', help_text='Warning any input here will override the group colors!', null=True, max_length=800, blank=True),
        ),
    ]
