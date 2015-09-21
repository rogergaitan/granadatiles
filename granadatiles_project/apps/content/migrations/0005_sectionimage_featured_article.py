# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
        ('content', '0004_initial_testimony_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionimage',
            name='featured_article',
            field=models.ForeignKey(null=True, related_name='featured_article', blank=True, to='news.Article'),
        ),
    ]
