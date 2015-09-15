# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0002_initial_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tilesize',
            options={'verbose_name': 'Size', 'verbose_name_plural': 'Sizes'},
        ),
        migrations.AddField(
            model_name='collection',
            name='featured',
            field=models.BooleanField(verbose_name='Featured', default=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='menu_image',
            field=sorl.thumbnail.fields.ImageField(default='', upload_to='Galleries/menu'),
        ),
        migrations.AddField(
            model_name='collection',
            name='show_in_menu',
            field=models.BooleanField(verbose_name='Show in menu', default=True),
        ),
    ]
