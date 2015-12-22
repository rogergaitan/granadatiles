# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0035_layout_portfolio'),
    ]

    operations = [
        migrations.AddField(
            model_name='layout',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='layouts', verbose_name='Image', null=True, blank=True),
        ),
    ]
