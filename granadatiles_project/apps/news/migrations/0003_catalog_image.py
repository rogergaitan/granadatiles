# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150921_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='image',
            field=models.ImageField(verbose_name='Image', default='image.png', upload_to='Catalog'),
            preserve_default=False,
        ),
    ]
