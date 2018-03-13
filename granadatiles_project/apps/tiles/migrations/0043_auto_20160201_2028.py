# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0042_auto_20160111_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='layout',
            name='image',
            field=models.FileField(verbose_name='Image', null=True, blank=True, upload_to='layouts'),
        ),
    ]
