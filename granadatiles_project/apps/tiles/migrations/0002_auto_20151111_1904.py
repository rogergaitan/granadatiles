# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='slug_es',
            field=models.SlugField(null=True, unique=True, max_length=35),
        ),
        migrations.AlterField(
            model_name='group',
            name='slug_es',
            field=models.SlugField(null=True, unique=True, max_length=35),
        ),
        migrations.AlterUniqueTogether(
            name='tiledesign',
            unique_together=set([('name', 'group')]),
        ),
    ]
