# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0016_collectioncontent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collectioncontent',
            name='menu',
        ),
    ]
