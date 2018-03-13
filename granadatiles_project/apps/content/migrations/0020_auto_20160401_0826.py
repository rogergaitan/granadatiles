# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0019_auto_20160324_1854'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='area',
            options={'ordering': ['title'], 'verbose_name_plural': 'Manageable Areas', 'verbose_name': 'Manageable Area'},
        ),
        migrations.AlterModelOptions(
            name='featuredvideo',
            options={'ordering': ['order'], 'verbose_name_plural': 'Videos', 'verbose_name': 'Video'},
        ),
        migrations.AlterModelOptions(
            name='indexnavigation',
            options={'ordering': ['title'], 'verbose_name_plural': 'Index Links', 'verbose_name': 'Index Link'},
        ),
        migrations.AlterModelOptions(
            name='testimony',
            options={'ordering': ['title'], 'verbose_name_plural': 'Testimonials', 'verbose_name': 'Testimony'},
        ),
    ]
