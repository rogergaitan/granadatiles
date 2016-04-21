# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0064_auto_20160418_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShippingData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity_uom', models.CharField(verbose_name='Quantity Unit Of Measure', max_length=30)),
                ('freigth_class', models.CharField(verbose_name='Freight Class', max_length=10)),
            ],
            options={
                'verbose_name': 'Shipping Data',
                'verbose_name_plural': 'Shipping Data',
            },
        ),
        migrations.AddField(
            model_name='collection',
            name='shipping_data',
            field=models.ForeignKey(verbose_name='Shipping Data', blank=True, null=True, to='tiles.ShippingData'),
        ),
    ]
