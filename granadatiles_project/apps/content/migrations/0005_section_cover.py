# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.db import models, migrations
from django.conf import settings
from django.utils import timezone

def addInitialData(apps, schema_editor):
    if settings.DEBUG == True:
        Section = apps.get_model('content', 'section')
        sections = Section.objects.order_by('id')

        Photographer = apps.get_model('galleries', 'photographer')
        photographer = Photographer.objects.create(name='Ryan Phillips')

        Designer = apps.get_model('galleries', 'designer')
        designer = Designer.objects.create(name='Deindre Doherty')

        Article = apps.get_model('news', 'article')
        featured_article = Article.objects.create(
            title='Bath of the Month Oct 2013',
            description='Lorem ipsum dolor sit amet, consectetur adipiscing elit',
            image=os.path.join(settings.STATIC_URL, 'img/initial/news/article/House_Beautiful_cover.jpg'),
            url='',
            date=timezone.now(),
            magazine_id=1
        )

        section1 = sections[0]

        section_image = section1.images.create(
            designer_id=designer.id,
            photographer_id=photographer.id,
            featured_article_id=featured_article.id,
            image=os.path.join(settings.STATIC_URL, 'img/initial/content/Cluny-on-bath-Granada-tile-cement.jpg')
        )

        Magazine = apps.get_model('news', 'magazine')
        magazines = Magazine.objects.bulk_create([
            Magazine(
              name='HouseBeautiful',
              logo=os.path.join(settings.STATIC_URL, 'img/initial/news/House-Beautiful-Granada-Tile-cement.png')
            ),

            Magazine(
                name='Dwell',
                logo=os.path.join(settings.STATIC_URL, 'img/initial/news/Dwell-Granada-Tile-cement.png')
            ),
            Magazine(
                name='Marta Living',
                logo=os.path.join(settings.STATIC_URL, 'img/initial/news/Martha-Living-Granada-Tile-cement.png')
            ),
            Magazine(
                name='AD',
                logo=settings.STATIC_URL + 'img/initial/news/AD-Granada-Tile-cement.png'
            ),
            Magazine(
                name='Elle Decor',
                logo=os.path.join(settings.STATIC_URL, 'img/initial/news/Elle-Decor-Granada-Tile-cement.png')
            ),
        ])

        section_image.articles.create(
                title='Lorep ipsum',
                description='Lorem ipsum dolor sit amet, consectetur adipiscing elit',
                image=os.path.join(settings.STATIC_URL, 'img/initial/news/article/Magazine-Dwell-Granada-Tile.jpg'),
                url='http://www.dwell.com/',
                magazine_id=2,
                date=timezone.now()
        )

        section_image.articles.create(
                title='Lore ipsum',
                description='Lorem ipsum dolor sit amet, consectetur adipiscing elit',
                image=os.path.join(settings.STATIC_URL, 'img/initial/news/article/Magazine-Coastal-Living-Granada-Tile.jpg'),
                url='http://www.coastalliving.com/',
                magazine_id=3,
                date=timezone.now()
        )

        section_image.articles.create(
                title='Lorep ipsum',
                description='Lorem ipsum dolor sit amet, consectetur adipiscing elit',
                image=os.path.join(settings.STATIC_URL, 'img/initial/news/article/cover_AD.jpg'),
                url='http://www.revistaad.es/',
                magazine_id=4,
                date=timezone.now()
        )

        section_image.articles.create(
                title='Lorep ipsum',
                description='Lorem ipsum dolor sit amet, consectetur adipiscing elit',
                image=os.path.join(settings.STATIC_URL, 'img/initial/news/article/elle_decor_cover.jpeg'),
                url='http://www.elledecor.com/',
                magazine_id=5,
                date=timezone.now()
        )


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_initial_testimony_data'),
        ('tiles', '0002_initial_data')
    ]

    operations = [
        migrations.RunPython(addInitialData)
    ]
