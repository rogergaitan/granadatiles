# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
        ('tiles', '0043_auto_20160201_2028'),
        ('content', '0015_instock_sections'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionContent',
            fields=[
                ('flatpage_ptr', models.OneToOneField(parent_link=True, primary_key=True, serialize=False, auto_created=True, to='flatpages.FlatPage')),
                ('title_es', models.CharField(max_length=200, blank=True, null=True)),
                ('content_es', models.TextField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(help_text='El orden en el que aparecera en el menu selecciondado despues de los elementos predefinidos', verbose_name='Order')),
                ('menu', models.IntegerField(default=1, choices=[(1, 'Collection Content')])),
                ('cover', sorl.thumbnail.fields.ImageField(blank=True, upload_to='', verbose_name='Cover', null=True)),
                ('collection', models.ForeignKey(to='tiles.Collection', verbose_name='collection', related_name='content')),
            ],
            options={
                'verbose_name_plural': 'Collection content',
                'verbose_name': 'Collection content',
                'ordering': ('order',),
            },
            bases=('flatpages.flatpage',),
        ),
    ]
