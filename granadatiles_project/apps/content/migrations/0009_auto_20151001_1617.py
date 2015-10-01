# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_section_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sectionimage',
            name='articles',
            field=models.ManyToManyField(to='news.Article', blank=True),
        ),
    ]
