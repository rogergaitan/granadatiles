# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='title_pr',
        ),
        migrations.RemoveField(
            model_name='galleryoptions',
            name='title_pr',
        ),
        migrations.RemoveField(
            model_name='galleyimages',
            name='description_pr',
        ),
        migrations.RemoveField(
            model_name='galleyimages',
            name='title_pr',
        ),
    ]
