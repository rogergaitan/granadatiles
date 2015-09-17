# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def addInitialData(apps, schema_editor):
    social = apps.get_model('content', 'Social')
    social.objects.bulk_create([
            #1
            social(
                    name='Facebook',
                    url='https://www.facebook.com/GranadaTile/',
                    order=1,
                    active=True,
                    css_class='facebook'
                ),
            #2
            social(
                    name='Twitter',
                    url='https://twitter.com/GranadaTile',
                    order=2,
                    active=True,
                    css_class='twitter'
                ),
            #3
            social(
					name='Linked In',
					url='https://www.linkedin.com/company/granada-tile',
					order=3,
					active=True,
					css_class='linked-in'
				),
            
            social(
					name='RSS',
					url='',
					order=4,
					active=True,
					css_class='rss'
				),
			
			social(
					name='Yelp',
					url='',
					order=5,
					active=True,
					css_class='yelp'
				),
			
			social(
					name='Pinterest',
					url='https://www.pinterest.com/granadatile/',
					order=6,
					active=True,
					css_class='pinterest'
				),
			
			social(
					name='Instagram',
					url='',
					order=7,
					active=True,
					css_class='instagram'
				),
			
			social(
					name='Houzz',
					url='https://www.houzz.com/Granada-Tile',
					order=8,
					active=True,
					css_class='houzz'
				),
        ])


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_initial_data'),
    ]

    operations = [
        migrations.RunPython(addInitialData)
    ]
