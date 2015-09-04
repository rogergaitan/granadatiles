# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20150904_2013'),
        ('tiles', '0002_auto_20150904_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='section_image',
            field=models.ForeignKey(to='content.SectionImage', default=''),
            preserve_default=False,
        ),
    ]
