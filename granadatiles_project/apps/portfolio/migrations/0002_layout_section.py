# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def addInitialData(apps, schema_editor):
    Section = apps.get_model('content', 'section')
    Section.objects.bulk_create([
                Section(
                        name='Layouts',
                        name_es='Diseños',
                        title='Layouts',
                        title_es='Diseños',
                        description='''Lorem ipsum dolor sit amet, consectetur 
                        adipiscing elit. Mauris quis ipsum lectus. 
                        Phasellus placerat sem quis ante molestie 
                        malesuada. Maecenas ﬁnibus justo ac nulla
                        feugiat dapibus. In hac habitasse platea dictumst. 
                        Suspendisse scelerisque auctor ipsum. Nulla vitae enim 
                        blandit nisl malesuada cursus nec eget 
                        velit. Mauris eu eleifend lacus.'''
                    )
         ])


class Migration(migrations.Migration):


    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(addInitialData)
    ]
