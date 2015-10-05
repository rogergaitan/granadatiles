# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.conf import settings
from django.db import models, migrations

def addInitialData(apps, schema_editor):

    collection = apps.get_model('tiles', 'Collection')
    collection.objects.bulk_create([
        collection(
            title='Echo Tile Collection',
            title_es='',
            slug='echo',
            slug_es='echo',
            description='''<ul><li>Original French art form</li>
            <li>Cement tiles are cured, not fired</li>
            <li>Organic colors</li><li>Industrial strength</li>
            <li>Pressed to 2,000 lbs. per square inch<br></li></ul>''',
            description_es='',
            image=os.path.join(settings.STATIC_URL, 'img/initial/tiles/FairweatherBar-compressor-compressor.jpg'),
            menu_image=''
        ),
        collection(
            title='Minis Tile Collection',
            title_es='',
            slug='minis',
            slug_es='minis',
            description='''<ul><li>Mozaic size cement tiles</li>
            <li>Geometric shapes</li>
            <li>Use on bathroom floors and walls</li>
            <li>Use on kitchen floors and backsplashes</li></ul>''',
            description_es='',
            image=os.path.join(settings.STATIC_URL,
                'img/initial/tiles/heath-ceramics-mural-tile-and-clay-studio-photo-by-mariko-reed-compressor-com_RdqFIFZ.jpg'),
            menu_image=''
        ),
        collection(
            title='Andalucía Tile Collection',
            title_es='',
            slug='mauresque',
            slug_es='mauresque',
            description='''<ul><li>Inspired by France and Morocco</li>
            <li>Variety of shapes and sizes</li>
            <li>Use on bathroom floors and walls, kitchen backsplashes and more</li></ul>''',
            description_es='',
            image=os.path.join(settings.STATIC_URL, 'img/initial/tiles/kitchen-minis-compressor_ca6NA4u.jpg'),
            menu_image=''
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
            image=os.path.join(settings.STATIC_URL,
                               'img/initial/tiles/groups/Designer-Erin-Adams-Granada-Tile-Cement.jpg'),
            collection=echo_collection
        ),
        group(
            title='Mediterranean',
            title_es='',
            description='Lorem ipsum dolor sit amet consectetur adipsicing',
            description_es='',
            image=os.path.join(settings.STATIC_URL,
                               'img/initial/tiles/groups/Essential-Shapes-Granada-Tile-Cement.jpg'),
            collection=echo_collection
        ),
        group(
            title='Moroccan',
            title_es='',
            description='Lorem ipsum dolor sit amet consectetur adipsicing',
            description_es=os.path.join(settings.STATIC_URL,
                                        'img/initial/tiles/groups/Mediterranean-Granada-Tile\-Cement.jpg'),
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
            image=os.path.join(settings.STATIC_URL,
                               'img/initial/tiles/groups/Moroccan-Granada-Tile-Cement.jpg'),
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
