# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models, migrations


def addInitialData(apps, schema_editor):
    testimony = apps.get_model('content', 'Testimony')
    if settings.DEBUG == True:
        testimony.objects.bulk_create([
                #1
                testimony(
                        title='Krista Schwartz, Principal',
                        title_es='',
                        description='We wrapped up our lower level bar project and I want to share it with you. Everyone comments on the tile! Thanks for making a great product clients can be proud of.',
                        description_es='',
                        subtitle='Indicia LLC Saint Paul, MN',
                        subtitle_es=''
                    ),
                #2
                testimony(
                        title='Sed magna nibh',
                        title_es='',
                        description='Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Duis malesuada ullamcorper at.',
                        description_es='',
                        subtitle='Country and Date',
                        subtitle_es=''
                    ),
                #3
                testimony(
                        title='Sed magna nibh',
                        title_es='',
                        description='Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Duis malesuada ullamcorper at.',
                        description_es='',
                        subtitle='Country and Date',
                        subtitle_es=''
                    ),
            ])

class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_initial_social'),
    ]

    operations = [
        migrations.RunPython(addInitialData)
    ]
