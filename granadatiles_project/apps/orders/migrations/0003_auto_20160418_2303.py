# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20160418_1608'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='credit_cart_number',
            new_name='credit_card_number',
        ),
    ]
