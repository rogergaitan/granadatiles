# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0013_extendedflatpage_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendedflatpage',
            name='content_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='extendedflatpage',
            name='title_es',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='extendedflatpage',
            name='menu',
            field=models.IntegerField(default=1, choices=[(1, 'Product Information'), (2, 'News/Press'), (3, 'About Us')]),
        ),
    ]
