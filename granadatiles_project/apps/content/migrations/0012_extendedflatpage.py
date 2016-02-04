# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
        ('content', '0011_auto_20151204_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedFlatPage',
            fields=[
                ('flatpage_ptr', models.OneToOneField(primary_key=True, to='flatpages.FlatPage', parent_link=True, auto_created=True, serialize=False)),
                ('order', models.PositiveIntegerField(help_text='El orden en el que aparecera en el menu selecciondado despues de los elementos predefinidos', verbose_name='Order')),
                ('menu', models.IntegerField(default=1, choices=[(1, 'Collections'), (2, 'News/Press'), (3, 'About Us')])),
            ],
            options={
                'ordering': ('order',),
                'verbose_name_plural': 'flat pages',
                'verbose_name': 'flat page',
            },
            bases=('flatpages.flatpage',),
        ),
    ]
