# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0066_auto_20160427_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tile',
            name='plane',
        ),
        migrations.RemoveField(
            model_name='tile',
            name='rotate_deg1',
        ),
        migrations.RemoveField(
            model_name='tile',
            name='rotate_deg2',
        ),
        migrations.RemoveField(
            model_name='tile',
            name='rotate_deg3',
        ),
        migrations.RemoveField(
            model_name='tile',
            name='rotate_deg4',
        ),
        migrations.RemoveField(
            model_name='tile',
            name='thickness',
        ),
        migrations.RemoveField(
            model_name='tile',
            name='weight',
        ),
        migrations.AddField(
            model_name='tiledesign',
            name='plane',
            field=models.FileField(verbose_name='Plane', upload_to='designs', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tiledesign',
            name='rotate_deg1',
            field=models.PositiveIntegerField(default=0, choices=[(0, '0 deg'), (90, '90 deg'), (270, '270 deg'), (180, '180 deg')]),
        ),
        migrations.AddField(
            model_name='tiledesign',
            name='rotate_deg2',
            field=models.PositiveIntegerField(default=90, choices=[(0, '0 deg'), (90, '90 deg'), (270, '270 deg'), (180, '180 deg')]),
        ),
        migrations.AddField(
            model_name='tiledesign',
            name='rotate_deg3',
            field=models.PositiveIntegerField(default=270, choices=[(0, '0 deg'), (90, '90 deg'), (270, '270 deg'), (180, '180 deg')]),
        ),
        migrations.AddField(
            model_name='tiledesign',
            name='rotate_deg4',
            field=models.PositiveIntegerField(default=180, choices=[(0, '0 deg'), (90, '90 deg'), (270, '270 deg'), (180, '180 deg')]),
        ),
        migrations.AddField(
            model_name='tiledesign',
            name='thickness',
            field=models.CharField(verbose_name='Thickness', max_length=10, null=True, default=''),
        ),
        migrations.AddField(
            model_name='tiledesign',
            name='weight',
            field=models.CharField(verbose_name='Weight', max_length=10, null=True, default=''),
        ),
    ]
