# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_initial_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='title_pr',
        ),
        migrations.RemoveField(
            model_name='custommessage',
            name='name_pr',
        ),
        migrations.RemoveField(
            model_name='custommessage',
            name='title_pr',
        ),
        migrations.RemoveField(
            model_name='featuredvideo',
            name='title_pr',
        ),
        migrations.RemoveField(
            model_name='images',
            name='description_image_pr',
        ),
        migrations.RemoveField(
            model_name='section',
            name='name_pr',
        ),
        migrations.RemoveField(
            model_name='section',
            name='title_pr',
        ),
        migrations.RemoveField(
            model_name='social',
            name='name_pr',
        ),
    ]
