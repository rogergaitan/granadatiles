# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0036_layout_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='plane',
            field=models.FileField(null=True, blank=True, upload_to='designs', verbose_name='Design'),
        ),
    ]
