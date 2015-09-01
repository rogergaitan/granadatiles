# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def addInitialData(apps, schema_editor):
	social = apps.get_model('content', 'Social')
	social.objects.bulk_create([
			#1
			social(
					name='facebook',
					name_es='',
					link='https://www.facebook.com',
					order=1,
					active=True
				),
			#2
			social(
					name='twitter',
					name_es='',
					link='https://twitter.com',
					order=2,
					active=True
				),
			#3
			social(
					name='youtube',
					name_es='',
					link='https://www.youtube.com',
					order=3,
					active=True
				),
		])


class Migration(migrations.Migration):

	dependencies = [
		('content', '0002_initial_data'),
	]

	operations = [
		migrations.RunPython(addInitialData)
	]
