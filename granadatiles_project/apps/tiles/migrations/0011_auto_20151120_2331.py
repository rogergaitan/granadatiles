# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0010_auto_20151118_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='PalleteColor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('name_es', models.CharField(null=True, max_length=150, verbose_name='Name_es', blank=True)),
                ('hexadecimalCode', models.CharField(max_length=20, verbose_name='Color')),
            ],
            options={
                'verbose_name_plural': 'Pallete Colors',
                'verbose_name': 'Pallete Color',
            },
        ),
        migrations.RemoveField(
            model_name='tile',
            name='colors',
        ),
        migrations.AddField(
            model_name='tile',
            name='colors',
            field=models.ManyToManyField(related_name='tiles', verbose_name='Tiles Colors', to='tiles.PalleteColor'),
        ),
    ]
