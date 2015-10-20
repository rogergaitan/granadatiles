# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def addInitialData(apps, schema_editor):
	video = apps.get_model('content', 'FeaturedVideo')
	video.objects.bulk_create([
			#1
			video(
				name='Granada Tile Revives the Fine Art of Making Cement Tiles',
				name_es='Granada Tile Revive el Fino Arte de hacer tejas de cemento',
				order=1,
				video='https://www.youtube.com/embed/GtWPVAHOQj4'
				),
			#1
			video(
				name='How to Install Cement Tile',
				name_es='Como instalar baldosas de cemento',
				order=2,
				video='https://www.youtube.com/embed/jdd_FzqprAk'
				),
		])


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_section_cover'),
    ]

    operations = [
    	migrations.RunPython(addInitialData)
    ]
