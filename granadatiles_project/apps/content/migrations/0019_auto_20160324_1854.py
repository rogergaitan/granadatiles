# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0018_auto_20160304_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectioncontent',
            name='menu_title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='collectioncontent',
            name='menu_title_es',
            field=models.CharField(default='', max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='extendedflatpage',
            name='menu_title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='extendedflatpage',
            name='menu_title_es',
            field=models.CharField(default='', max_length=200, blank=True),
        ),
    ]
