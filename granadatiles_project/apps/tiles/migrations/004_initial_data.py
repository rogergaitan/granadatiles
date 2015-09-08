# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def addInitialData(apps, schema_editor):
	collection = apps.get_model('tiles', 'Collection')
	collection.objects.bulk_create([
	    collection(
		    title='Echo Tile Collection',
		    title_es='',
			description='''<ul><li>Original French art form</li>
			<li>Cement tiles are cured, not fired</li>
			<li>Organic colors</li><li>Industrial strength</li>
			<li>Pressed to 2,000 lbs. per square inch<br></li></ul>''',
			description_es='',
			image='',
		),	
		collection(
			title='Minis Tile Collection',
			title_es='',
			description='''<ul><li>Mozaic size cement tiles</li>
			<li>Geometric shapes</li>
			<li>Use on bathroom floors and walls</li>
			<li>Use on kitchen floors and backsplashes</li></ul>''',
			description_es='',
			image='',
		),
		collection(
		    title='Mauresque Tile Collection',
		    title_es='',
		    description='''<ul><li>Inspired by France and Morocco</li>
		    <li>Variety of shapes and sizes</li>
		    <li>Use on bathroom floors and walls, kitchen backsplashes and more</li></ul>''',
		    description_es='',
		    image='',
		),
	])
		
	group = apps.get_model('tiles', 'Group')
	echo_collection = collection.objects.filter(title__contains='echo')
	group.objects.bulk_create([
	    group(
		    title='Essential Shapes',
		    title_es='',
		    description='Lorem ipsum dolor sit amet consectetur adipsicing',
		    description_es='',
		    image='',
		    collection=echo_collection
		),
		group(
		    title='Mediterranean',
		    title_es='',
		    description='Lorem ipsum dolor sit amet consectetur adipsicing',
		    description_es='',
		    image='',
		    collection=echo_collection
		),
		group(
		    title='Moroccan',
		    title_es='',
		    description='Lorem ipsum dolor sit amet consectetur adipsicing',
		    description_es='',
		    image='',
		    collection=echo_collection
		),
		group(
		    title='Designer Erin Adams',
		    title_es='',
		    description='''The customizable Echo Tile Collection offers: <br />
		    <ul><li>Over 140 hand made cement tile designs</li>
			<li>Array of styles and sizes</li>
			<li>For residential projects (bathrooms, kitchens, patios and more)</li>
			<li>For commercial projects (restaurants, cafes, hotels, spas, shops)</li>
			<li>For floors and walls</li>
		    </ul>''',
		    description_es='',
		    image='',
		    collection=echo_collection
		),
		
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0003_auto_20150907_1619'),
    ]

    operations = [
		migrations.RunPython(addInitialData)
    ]
