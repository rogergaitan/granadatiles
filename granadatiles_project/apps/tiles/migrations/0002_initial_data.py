# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.db import models, migrations

def addInitialData(apps, schema_editor):
    
    collection = apps.get_model('tiles', 'Collection')
    collection.objects.bulk_create([
        collection(
            title='Echo Tile Collection',
            title_es='',
            slug= 'echo',
            slug_es = 'echo',
            description='''<ul><li>Original French art form</li>
            <li>Cement tiles are cured, not fired</li>
            <li>Organic colors</li><li>Industrial strength</li>
            <li>Pressed to 2,000 lbs. per square inch<br></li></ul>''',
            description_es='',
            image= settings.STATIC_URL + 'initial/tiles/',
            menu_image = settings.STATIC_URL + 'initial/tiles/icon-Echo-Collection-Granada-Tile-Cement.jpg'
        ),
        collection(
            title='Minis Tile Collection',
            title_es='',
            slug= 'minis',
            slug_es = 'minis',
            description='''<ul><li>Mozaic size cement tiles</li>
            <li>Geometric shapes</li>
            <li>Use on bathroom floors and walls</li>
            <li>Use on kitchen floors and backsplashes</li></ul>''',
            description_es='',
            image= settings.STATIC_URL + 'initial/tiles/',
            menu_image = settings.STATIC_URL + 'initial/tiles/Icon-Minis-Collection-Granada-Tile-Cement.png'
        ),
        collection(
            title='Mauresque Tile Collection',
            title_es='',
            slug= 'mauresque',
            slug_es = 'mauresque',
            description='''<ul><li>Inspired by France and Morocco</li>
            <li>Variety of shapes and sizes</li>
            <li>Use on bathroom floors and walls, kitchen backsplashes and more</li></ul>''',
            description_es='',
            image= settings.STATIC_URL + 'initial/tiles/',
            menu_image = settings.STATIC_URL + 'initial/tiles/Icon-Mauresque-Collection-Granada-Tile-Cement.png'
        ),
    ])
        
    group = apps.get_model('tiles', 'Group')
    echo_collection = collection.objects.filter(title='Echo Tile Collection').first()
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
        ('tiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(addInitialData)
    ]
