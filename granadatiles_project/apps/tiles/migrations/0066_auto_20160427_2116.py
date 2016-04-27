# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0065_auto_20160421_2200'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='is_not_square',
            field=models.BooleanField(verbose_name='Is Not Square', default=False),
        ),
        migrations.AddField(
            model_name='tile',
            name='mosaic',
            field=sorl.thumbnail.fields.ImageField(verbose_name='Mosaic', upload_to='mosaic', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shippingdata',
            name='freigth_class',
            field=models.CharField(max_length=10, verbose_name='Freight Class', choices=[('50', '50'), ('60', '60'), ('65', '65'), ('70', '70'), ('77.5', '77.5'), ('85', '85'), ('92.5', '92.5'), ('100', '100'), ('125', '125'), ('150', '150'), ('175', '175'), ('200', '200'), ('250', '250'), ('300', '300'), ('400', '400'), ('500', '500')]),
        ),
        migrations.AlterField(
            model_name='shippingdata',
            name='quantity_uom',
            field=models.CharField(max_length=30, verbose_name='Quantity Unit Of Measure', choices=[('BAG', 'BAG'), ('BOXES', 'BOXES'), ('BUNDLES', 'BUNDLES'), ('CARTONS', 'CARTONS'), ('CASES', 'CASES'), ('CRATES', 'CRATES'), ('DRUMS', 'DRUMS'), ('LOOSE', 'LOOSE'), ('PAILS', 'PAILS'), ('PALLETS', 'PALLETS'), ('PIECES', 'PIECES'), ('POLES', 'POLES'), ('TOTES', 'TOTES'), ('ROLLS', 'ROLLS')]),
        ),
    ]
