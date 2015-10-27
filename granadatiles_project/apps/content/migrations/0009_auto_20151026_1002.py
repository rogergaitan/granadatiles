# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_auto_20151026_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexnavigation',
            name='link_es',
            field=models.URLField(verbose_name='Link_es', blank=True, null=True),
        ),
    ]
