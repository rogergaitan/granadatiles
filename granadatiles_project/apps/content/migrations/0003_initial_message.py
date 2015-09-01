# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def addInitialData(apps, schema_editor):
	message = apps.get_model('content', 'CustomMessage')
	message.objects.bulk_create([
			message(
					name='LogIn',
					name_es='',
					title='You are already registered with us',
					title_es='Usted ya está registrado con nosotros',
					description='We sent password recovery instructions to your email, please check your inbox and',
					description_es='',
				),
		])

class Migration(migrations.Migration):

	dependencies = [
		('content', '0002_initial_social'),
	]

	operations = [
		migrations.RunPython(addInitialData)
	]
