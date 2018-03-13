# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_extendedflatpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendedflatpage',
            name='cover',
            field=sorl.thumbnail.fields.ImageField(upload_to='', verbose_name='Cover', blank=True, null=True),
        ),
    ]
