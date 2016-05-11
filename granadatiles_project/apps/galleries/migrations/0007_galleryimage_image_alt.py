# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0006_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='image_alt',
            field=models.CharField(verbose_name='Image Alt', blank=True, max_length=150, null=True),
        ),
    ]
