# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0063_merge'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('street_building_house_line1', models.CharField(max_length=80)),
                ('house_apt_line2', models.CharField(max_length=80)),
                ('zipcode', models.CharField(max_length=20)),
                ('province_state', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=80)),
                ('type', models.CharField(choices=[(1, 'Billing'), (2, 'Shipping')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('customer_first_name', models.CharField(verbose_name='Customer First Name', max_length=30)),
                ('customer_last_name', models.CharField(verbose_name='Customer Last Name', max_length=30)),
                ('customer_company_name', models.CharField(verbose_name='Customer Company Name', max_length=50)),
                ('credit_cart_number', models.CharField(blank=True, verbose_name='Credit Card Number', null=True, max_length=12)),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP Address')),
                ('same_as_shipping', models.BooleanField()),
                ('user', models.ForeignKey(blank=True, related_name='+', to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('input_sq_ft', models.PositiveIntegerField()),
                ('price_per_sq_ft', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_per_tile', models.DecimalField(decimal_places=2, max_digits=10)),
                ('base_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('box', models.ForeignKey(to='tiles.Box')),
                ('customized_tile', models.ForeignKey(blank=True, to='tiles.CustomizedTile', null=True)),
                ('order', models.ForeignKey(to='orders.Order')),
                ('tile', models.ForeignKey(blank=True, to='tiles.Tile', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='order',
            field=models.ForeignKey(to='orders.Order'),
        ),
    ]
