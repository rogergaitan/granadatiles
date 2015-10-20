# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('list_id', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('full_name', models.CharField(max_length=250, verbose_name='Full name')),
                ('is_active', models.BooleanField(verbose_name='Is Active')),
                ('sublevel', models.IntegerField(verbose_name='Sublevel')),
                ('sales_price', models.FloatField(verbose_name='Sales Price')),
                ('quantity_on_hand', models.IntegerField()),
                ('average_cost', models.FloatField(verbose_name='Average Cost')),
                ('quantity_on_order', models.IntegerField()),
                ('quantity_on_sales_order', models.FloatField()),
                ('sales_desc', models.CharField(max_length=250, verbose_name='Sales Description')),
                ('purchase_desc', models.CharField(max_length=250, verbose_name='Purchase Description')),
                ('purchase_cost', models.FloatField(verbose_name='Purchase Cost')),
            ],
            options={
                'verbose_name_plural': 'Items',
                'verbose_name': 'Item',
            },
        ),
    ]
