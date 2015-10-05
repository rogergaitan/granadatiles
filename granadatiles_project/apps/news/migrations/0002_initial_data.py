# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import datetime

from django.db import models, migrations
from django.conf import settings

def addInitialData(apps, schema_editor):
    if settings.DEBUG == True:
        Article = apps.get_model('news', 'article')

        Magazine = apps.get_model('news', 'magazine')

        afar = Magazine.objects.create(name='AFAR',
            logo=os.path.join(settings.STATIC_URL, 'img/initial/news/article/Magazine-Affar-Granada-Tile-Cement.jpg'))

        chatelaine = Magazine.objects.create(name='CHATELAINE',
            logo=os.path.join(settings.STATIC_URL, 'img/initial/news/article/Magazine-Chatelaine-Granada-Tile.jpg'))

        Article.objects.bulk_create([
            Article(
                      image=os.path.join(settings.STATIC_URL,
                            'img/initial/news/article/Magazine-Affar-Granada-Tile-Cement.jpg'),
                      title='DESIGNING L.A.',
                      magazine_id=afar.id,
                      description='''“The textures it creates are just amazing.” The Fez tile she used became Granada Tile’s
                                 best seller after Bestor used it in Intelligentsia’s ﬁrst L.A. cafe.''',
                      date=datetime.date(2015, 4, 28)
               ),

           Article(
                   image=os.path.join(settings.STATIC_URL,
                         'img/initial/news/article/Magazine-Chatelaine-Granada-Tile.jpg'),
                     title='BOLD & FEARLESS',
                     magazine_id=chatelaine.id,
                     description='''PUT THE EMPHASIS ON FLOORS WITH PATTERNS. Commiting to a graphic ﬂoor tile takes guts,
                                but he payoﬀ is huge. Jessica chose a Morocco-inspired cement ﬂoor for this kitchen.''',
                     date=datetime.date(2015, 4, 28)
              ),

          Article(
                  image=os.path.join(settings.STATIC_URL,
                        'img/initial/news/article/Magazine-Coastal-Living-Granada-Tile.jpg'),
                    title='DESIGNING L.A.',
                    magazine_id=afar.id,
                    description='''“The textures it creates are just amazing.” The Fez tile she used became Granada Tile’s
                                 best seller after Bestor used it in Intelligentsia’s ﬁrst L.A. cafe.''',
                    date=datetime.date(2015, 4, 28)
              ),

          Article(
                  image=os.path.join(settings.STATIC_URL,
                       'img/initial/news/article/Magazine-Chatelaine-Granada-Tile.jpg'),
                    title='BOLD & FEARLESS',
                    magazine_id=chatelaine.id,
                    description='''PUT THE EMPHASIS ON FLOORS WITH PATTERNS. Commiting to a graphic ﬂoor tile takes guts,
                                but he payoﬀ is huge. Jessica chose a Morocco-inspired cement ﬂoor for this kitchen.''',
                    date=datetime.date(2015, 4, 28)
              ),

          Article(
                  image=os.path.join(settings.STATIC_URL,
                       'img/initial/news/article/Magazine-Dwell-Granada-Tile.jpg'),
                    title='DESIGNING L.A.',
                    magazine_id=afar.id,
                    description='''“The textures it creates are just amazing.” The Fez tile she used became Granada Tile’s
                                 best seller after Bestor used it in Intelligentsia’s ﬁrst L.A. cafe.''',
                    date=datetime.date(2015, 4, 28)
              ),

          Article(
                  image=os.path.join(settings.STATIC_URL,
                       'img/initial/news/article/Magazine-HGTV-Granada-Tile.jpg'),
                    title='BOLD & FEARLESS',
                    magazine_id=chatelaine.id,
                    description='''PUT THE EMPHASIS ON FLOORS WITH PATTERNS. Commiting to a graphic ﬂoor tile takes guts,
                                but he payoﬀ is huge. Jessica chose a Morocco-inspired cement ﬂoor for this kitchen.''',
                    date=datetime.date(2015, 4, 28)
             ),
        ])

        Catalog = apps.get_model('news', 'catalog')
        Catalog.objects.bulk_create([
            Catalog(
                name = 'Instack Catalog 2015',
                image = os.path.join(settings.STATIC_URL,
                            'img/initial/news/catalog/News-In-Stock-Catalog-2015-Granada-Tile.jpg'),
            ),

            Catalog(
                name = 'Echo Collection Mini Catalog',
                image = os.path.join(settings.STATIC_URL,
                            'img/initial/news/catalog/News-Echo-Collection-Mini-Catalog-Granada-Tile.jpg'),
            ),

            Catalog(
                name = 'Instock Catalog 2015',
                image = os.path.join(settings.STATIC_URL,
                            'img/initial/news/catalog/News-Look-Book-2015-Granada-Tile.jpg'),
            ),

            Catalog(
                name = 'Lookbook 2013',
                image = os.path.join(settings.STATIC_URL,
                            'img/initial/news/catalog/News-Look-Book-2013-Granada-Tile.jpg'),
            ),

            Catalog(
                name = 'Lookbook 2013 - Volume 2',
                image = os.path.join(settings.STATIC_URL,
                            'img/initial/news/catalog/News-Look-Book-2013-vol2-Granada-Tile.jpg'),
            ),

            Catalog(
                name = 'Lookbook 2013 - Volume 1',
                image = os.path.join(settings.STATIC_URL,
                            'img/initial/news/catalog/News-Look-Book-2012-Granada-Tile.jpg'),
            ),

        ])


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(addInitialData)
    ]
