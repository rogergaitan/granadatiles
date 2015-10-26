# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import os
from django.conf import settings

def addInitialData(apps, schema_editor):
    IndexNavigation = apps.get_model('content', 'IndexNavigation')
    IndexNavigation.objects.bulk_create([
            IndexNavigation(
                title = 'Residential',
                title_es = 'Residencial',
                description = '''See examples of our cement tiles in
                                    kitchens, bathrooms, and outdoors.
                                    Normandy or Clunny.''',
                description_es = '''Vea ejemplos de nuestros azulejos de cemento
                                    en cocinas, baños y exteriores. 
                                    Normandía o Cluny.''',
                action_name = '''View our residential installations''',
                action_name_es = '''Mire nuestras instalaciones residenciales''',
                link = '/en/gallery/',
                link_es = '/es/galeria/',
                target = False,
                image = os.path.join(settings.STATIC_URL, 'img/initial/content/residential.png')
                ),

             IndexNavigation(
                title = 'Commercial',
                title_es = 'Comercial',
                description = '''See examples of our cement tiles in
                                    restaurants, cafes, resorts, hotels,
                                    spas, shops and offices.''',
                description_es = '''Vea ejemplos de nuestros azulejos de cemento
                                    en restaurantes, cafés, resorts, hoteles, spas,
                                    tiendas y oficinas.''',
                action_name = '''View our commercial Installations''',
                action_name_es = '''Mire nuestras instalaciones comerciales''',
                link = '/en/gallery/',
                link_es = '/es/galeria/',
                target = False,
                image = os.path.join(settings.STATIC_URL, 'img/initial/content/commercial.png')
                ),

             IndexNavigation(
                title = 'In Stock',
                title_es = 'En existencia',
                description = '''Cement tiles in stock in California,
                                    New Jersey and Texas distribution
                                    centers. Ships in 1-3 business days.''',
                description_es = '''Azulejos de cemento disponbles en los
                                    centros de distribucion de California,
                                    New Jersey y Texas. Entregas en 1-3 dias laborales.''',
                action_name = '''Shop in stock tiles - Available now!''',
                action_name_es = '''Compre azulejos - Disponibles ahora''',
                target = False,
                image = os.path.join(settings.STATIC_URL, 'img/initial/content/in_stock.png')
                ),

             IndexNavigation(
                title = 'Custom',
                title_es = 'Personalizados',
                description = '''Customize your cement tiles with 32
                                    colors and hundreds of designs.''',
                description_es = '''Personaliza tu azulejo de cemento con
                                    32 colores y cientos de diseños.''',
                action_name = '''Shop custom tiles''',
                action_name_es = '''Comprar azulejos personalizados''',
                target = False,
                image = os.path.join(settings.STATIC_URL, 'img/initial/content/custom.png')
                ),

        ])
    


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20151026_1002'),
    ]

    operations = [
        migrations.RunPython(addInitialData)
    ]
