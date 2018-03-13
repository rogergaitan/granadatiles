# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0055_auto_20160322_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='import_colors',
            field=models.CharField(max_length=50, verbose_name='Import Colors', null=True),
        ),
    ]
