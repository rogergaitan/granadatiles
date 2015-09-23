# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_auto_20150922_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionimage',
            name='articles',
            field=models.ManyToManyField(blank=True, to='news.Article', null=True),
        ),
        migrations.AlterField(
            model_name='sectionimage',
            name='designer',
            field=models.ForeignKey(blank=True, verbose_name='Designer', to='galleries.Designer', related_name='covers', null=True),
        ),
    ]
