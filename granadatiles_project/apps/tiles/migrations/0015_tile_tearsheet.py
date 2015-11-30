# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0014_auto_20151126_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='tearsheet',
            field=models.FileField(blank=True, verbose_name='Tearsheet', null=True, upload_to='tearsheets'),
        ),
    ]
