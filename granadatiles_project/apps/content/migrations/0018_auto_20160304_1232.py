# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0017_remove_collectioncontent_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectioncontent',
            name='menu_title',
            field=models.TextField(max_length=200, default=''),
        ),
        migrations.AddField(
            model_name='collectioncontent',
            name='menu_title_es',
            field=models.TextField(blank=True, max_length=200, default=''),
        ),
        migrations.AddField(
            model_name='extendedflatpage',
            name='menu_title',
            field=models.TextField(max_length=200, default=''),
        ),
        migrations.AddField(
            model_name='extendedflatpage',
            name='menu_title_es',
            field=models.TextField(blank=True, max_length=200, default=''),
        ),
    ]
