# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_sectionimage_featured_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sectionimage',
            name='description',
        ),
        migrations.RemoveField(
            model_name='sectionimage',
            name='description_es',
        ),
        migrations.RemoveField(
            model_name='sectionimage',
            name='link',
        ),
        migrations.RemoveField(
            model_name='sectionimage',
            name='target',
        ),
        migrations.RemoveField(
            model_name='sectionimage',
            name='title',
        ),
        migrations.RemoveField(
            model_name='sectionimage',
            name='title_es',
        ),
        migrations.AlterField(
            model_name='sectionimage',
            name='image',
            field=models.ImageField(upload_to='Covers'),
        ),
    ]
