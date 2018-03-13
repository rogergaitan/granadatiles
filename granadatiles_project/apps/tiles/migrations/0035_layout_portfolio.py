# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0034_layout'),
    ]

    operations = [
        migrations.AddField(
            model_name='layout',
            name='portfolio',
            field=models.ForeignKey(verbose_name='Portfolio', to='tiles.Portfolio', related_name='layouts', default=False),
        ),
    ]
