# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0003_style'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='style',
            options={'verbose_name': 'Style', 'verbose_name_plural': 'Styles'},
        ),
        migrations.AddField(
            model_name='collection',
            name='introduction',
            field=models.TextField(verbose_name='Introduction', default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='introduction_es',
            field=models.TextField(verbose_name='Introduction_es', null=True, blank=True),
        ),
    ]
