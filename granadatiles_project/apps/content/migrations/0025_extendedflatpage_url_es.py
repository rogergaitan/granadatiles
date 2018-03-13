# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0024_auto_20160509_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendedflatpage',
            name='url_es',
            field=models.CharField(null=True, max_length=100, verbose_name='URL_ES', blank=True, db_index=True),
        ),
    ]
