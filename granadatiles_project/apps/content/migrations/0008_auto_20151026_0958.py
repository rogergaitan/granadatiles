# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_indexnavigation'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexnavigation',
            name='action_name',
            field=models.CharField(verbose_name='Action Name', max_length=200, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='indexnavigation',
            name='action_name_es',
            field=models.CharField(blank=True, verbose_name='Action Name_es', max_length=200, null=True),
        ),
    ]
