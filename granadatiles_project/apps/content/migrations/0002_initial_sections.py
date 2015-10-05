# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def addInitialData(apps, schema_editor):
    Section = apps.get_model('content', 'Section')
    Section.objects.bulk_create([
            #1    
            Section(
                    name='Home',
                    name_es='Inicio',
                    title='',
                    title_es='',
                    description='',
                    description_es=''
                ),
            #2
            Section(
                    name='Collections/Compare our products',
                    name_es='Colecciones/Compare nuestros productos',
                    title='Compare our Products ',
                    title_es='Compare our Products ',
                    description='''This Tile Comparison Chart is designed to give you an overview of Granada Tile's 
                                    6 cement and concrete tile collections, with their varied characteristics and uses.''',
                    description_es='''This Tile Comparison Chart is designed to give you an overview of Granada Tile's 
                                    6 cement and concrete tile collections, with their varied characteristics and uses.'''
                ),
             #3
            Section(
                    name='Collections/Cements vs Ceramic',
                    name_es='Colecciones/ Cemento vs Ceramica',
                    title='Cement and Concrete Tile vs. Ceramic Tile - Comparison ',
                    title_es='Cement and Concrete Tile vs. Ceramic Tile - Comparison ',
                    description='''This section compares cement / concrete tile to ceramic tile primarily from the environmental 
                                   and durability perspectives. Since there exists a great deal of variability within cement''',
                    description_es='''This section compares cement / concrete tile to ceramic tile primarily from the environmental
                                      and durability perspectives. Since there exists a great deal of variability within cement'''
                ),
            #4
            Section(
                    name='Collections/Color Pallete',
                    name_es='Colecciones/ Paleta de colores',
                    title='Tile Color Palettes - Design Custom & Personalized Tile',
                    title_es='Tile Color Palettes - Design Custom & Personalized Tile',
                    description='''Each of Granada Tile's six collections of cement and concrete tile has its own unique 
                                    color palette. In the case of the Echo Collection, the tile color selection is extensive''',
                    description_es='''Each of Granada Tile's six collections of cement and concrete tile has its own unique color 
                                      palette. In the case of the Echo Collection, the tile color selection is extensive'''
                ),
            #5
            Section(
                    name='Gallery',
                    name_es='Galeria',
                    title='Photos of Cement & Concrete Tile Installation',
                    title_es='Editoriales de ceramica en revistas',
                    description='''Granada Tile is pleased to share photos of some of the cement tile installations
                                    using our ﬂagship Echo Collection tiles. Our hand made cement and concrete tiles
                                    have been used in private residences and commercial projects, indoors and outdoors, 
                                    and on ﬂoors and on walls (and even on ceilings). These cement and concrete tile 
                                    installation photos feature bathroom tile, kitchen tile, tile backslashes, wall tiles, 
                                    ﬂoor tiles, commercial tiles, restaurant tiles, spa tiles, and patio tiles.''',
                    description_es=''
                ),
            #6
           Section(
                    name='News/Press/Magazines',
                    name_es='Noticias/Prensa/Revistas',
                    title='Tile Editorials in Magazines ',
                    title_es='Tile Editorials in Magazines ',
                    description='''Magazines love Granada Tile. Click the covers to ﬁnd out what magazine
                                    editors are saying about our latest tile news. ''',
                    description_es='''Magazines love Granada Tile. Click the covers to ﬁnd out what magazine
                                    editors are saying about our latest tile news. '''
                ),
            #7
           Section(
                    name='News/Press/Catalog-Inspiration',
                    name_es='Noticias/Prensa/Catalogos-Inspiraciones',
                    title='Tile Design Inspiration to Help You Design Your Project',
                    title_es='Tile Design Inspiration to Help You Design Your Project',
                    description='''As we all know, design inspiration can come from many diﬀerent sources:
                                   a friend's home, a shop window, a photograph.''',
                    description_es='''As we all know, design inspiration can come from many diﬀerent sources:
                                      a friend's home, a shop window, a photograph.'''
                ),
            #8
            Section(
                    name='News/Press/Videos',
                    name_es='Noticias/Prensa/Videos',
                    title='Tile Videos - How to Tile Videos from Granada Tile',
                    title_es='Tile Videos - How to Tile Videos from Granada Tile',
                    description='''Ever wondered how cement tiles are made? Take a peak behind the 
                                   scenes at this remarkable technique developed a century and a half ago. ''',
                    description_es='''Ever wondered how cement tiles are made? Take a peak behind the 
                                      scenes at this remarkable technique developed a century and a half ago.'''
                ),
            #9
            Section(
                    name='About us',
                    name_es='Acerca de nosotros',
                    title='Contact Granada Tile Cement and Concrete Tile',
                    title_es='Contacta Grada Tile Cement and Concrete Tile',
                    description='''For all of your cement and concrete tile questions and needs,
                                contact Granada Tile by telephone, e-mail, Skype and fax. We want to hear from you!''',
                    description_es='''For all of your cement and concrete tile questions and needs,
                                contact Granada Tile by telephone, e-mail, Skype and fax. We want to hear from you!'''
                ),
            #10
            Section(
            name = 'Portafolio',
            name_es = 'Portafolio',
            title = 'Tiles in my Portfolio',
            title_es = 'Ladrillos en mi portafolio',
            description = '''My Portfolio is the home for all of your favorite tiles from across the Granada Tile collections. Don't go hunting through \
                           the website to try to find that one special tile you loved; save it to your Portfolio. Have you created a really great custom \
                           colorway tile in the Echo Collection Catalogue? Don't lose your work; save it to your Portfolio. Want to do a room layout? \
                           Use the tiles in your Portfolio to experiment with different combinations.''',
            description_es = '''My Portfolio is the home for all of your favorite tiles from across the Granada Tile collections. Don't go hunting through \
            the website to try to find that one special tile you loved; save it to your Portfolio. Have you created a really great custom \
            colorway tile in the Echo Collection Catalogue? Don't lose your work; save it to your Portfolio. Want to do a room layout? \
            Use the tiles in your Portfolio to experiment with different combinations.'''
        )
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
