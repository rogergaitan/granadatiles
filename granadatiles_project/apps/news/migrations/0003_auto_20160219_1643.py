# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_initial_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': 'Articles', 'verbose_name': 'Article', 'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='magazine',
            name='logo',
            field=models.ImageField(null=True, blank=True, upload_to='Magazines'),
        ),
    ]
