# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def addInitialData(apps, schema_editor):
    section = apps.get_model('content', 'Section')
    section.objects.bulk_create([
            section(
                    name='Magazines',
                    name_es='Revistas',
                    title='Tile Editorials in Magazines',
                    title_es='Editoriales de ceramica en revistas',
                    description='Magazines love Granada Tile. Click the covers to ﬁnd out what magazine editors are '
                                'saying about our latest tile news. See our tiles in magazines’ new product roundups and in articles featuring our tiles in residential and commercial projects',
                    description_es=''
                ),
            section(
                    name='Gallery',
                    name_es='Galeria',
                    title='Photos of Cement & Concrete Tile Installation',
                    title_es='Editoriales de ceramica en revistas',
                    description='Granada Tile is pleased to share photos of some of the cement tile installations using our ﬂagship Echo Collection tiles. Our hand made cement and concrete tiles have been used in private residences and commercial projects, indoors and outdoors, and on ﬂoors and on walls (and even on ceilings). These cement and concrete tile installation photos feature bathroom tile, kitchen tile, tile backslashes, wall tiles, ﬂoor tiles, commercial tiles, restaurant tiles, spa tiles, and patio tiles.',
                    description_es=''
                ),
            section(
                    name='Catalogs / Inspiration Books',
                    name_es='Catalogod / Libros fr Inspiracion',
                    title='Tile Design Inspiration to Help You Design Your Project ',
                    title_es='Tile Design Inspiration to Help You Design Your Project ',
                    description='As we all know, design inspiration can come from many diﬀerent sources: a friends home, a shop window, a photograph',
                    description_es=''
                ),
        ])

    Area = apps.get_model('content', 'Area')
    Area.objects.bulk_create([
            #1
            Area(
                    title='Footer',
                    title_es='Pie de pagina',
                    description='GrandaTile',
                    description_es=''
                ),
        ])


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(addInitialData)
    ]
