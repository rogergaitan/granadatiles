# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def addInitialData(apps, schema_editor):
    Section = apps.get_model('content', 'Section')
    Section.objects.bulk_create([
            #11    
            Section(
                    name='In Stock Samples',
                    name_es='Muestras disponibles',
                    title='In Stock Samples',
                    title_es='Muestras Disponibles',
                    description='''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                   Mauris quis ipsum lectus. Phasellus placerat sem quis ante 
                                   molestie malesuada. Maecenas ﬁnibus justo ac nulla feugiat dapibus.
                                   In hac habitasse platea dictumst. Suspendisse scelerisque auctor ipsum.
                                   Nulla vitae enim blandit nisl malesuada cursus nec eget velit. Mauris eu 
                                   eleifend lacus.''',
                    description_es=''
                ),
            #12
            Section(
                    name='In Stock Tiles',
                    name_es='Azulejos disponibles',
                    title='In Stock Tiles',
                    title_es='Azulejos Disponibles',
                    description='''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                                   Mauris quis ipsum lectus. Phasellus placerat sem quis ante 
                                   molestie malesuada. Maecenas ﬁnibus justo ac nulla feugiat dapibus.
                                   In hac habitasse platea dictumst. Suspendisse scelerisque auctor ipsum.
                                   Nulla vitae enim blandit nisl malesuada cursus nec eget velit. Mauris eu 
                                   eleifend lacus.''',
                    description_es=''
                ),
            ])


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0014_auto_20160204_1117'),
    ]

    operations = [
        migrations.RunPython(addInitialData)
    ]
