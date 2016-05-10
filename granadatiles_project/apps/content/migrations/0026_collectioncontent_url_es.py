# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0025_extendedflatpage_url_es'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectioncontent',
            name='url_es',
            field=models.CharField(db_index=True, verbose_name='URL_ES', max_length=100, null=True, blank=True),
        ),
    ]
