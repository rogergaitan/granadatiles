# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def addInitialData(apps, schema_editor):
	section = apps.get_model('content', 'Section')
	section.objects.bulk_create([
			section(
					name='Magazines',
					name_es='Revistas',
					name_pr='',
					title='Tile Editorials in Magazines ',
					title_es='Editoriales de ceramica en revistas',
					title_pr='',
					description='Magazines love Granada Tile. Click the covers to ﬁnd out what magazine editors are '
								'saying about our latest tile news. See our tiles in magazines’ new product roundups and in articles featuring our tiles in residential and commercial projects',
					description_es=''
				),
		])

	Area = apps.get_model('content', 'Area')
	Area.objects.bulk_create([
			#1
			Area(
					title='Footer',
					title_es='Pie de pagina',
					title_pr='',
					message='GrandaTile',
					message_es=''
				),
		])


class Migration(migrations.Migration):

	dependencies = [
		('content', '0001_initial'),
	]

	operations = [
		migrations.RunPython(addInitialData)
	]
