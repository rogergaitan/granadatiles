# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def addInitialData(apps, schema_editor):
    leadtime = apps.get_model('tiles', 'LeadTime')
    leadtime.objects.bulk_create([
        leadtime(
            title='In stock lead time',
            description='2-4 weeks for in stock tiles'
        ),

        leadtime(
            title='Custom lead time',
            description='8-10 weeks for all custom tiles'
        )

    ])


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0019_leadtime'),
    ]

    operations = [
        migrations.RunPython(addInitialData)
    ]
