# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.db import models, migrations
from django.conf import settings
from django.utils import timezone

def addInitialData(apps, schema_editor):
    if settings.DEBUG == True:
	    Section = apps.get_model('content', 'section')
	    section = Section.objects.create(
			title = '<h1>Tiles in my Portfolio</h1>',
	        description = "My Portfolio is the home for all of your favorite tiles from across the Granada Tile collections. Don't go hunting through \
	                       the website to try to find that one special tile you loved; save it to your Portfolio. Have you created a really great custom \
	                       colorway tile in the Echo Collection Catalogue? Don't lose your work; save it to your Portfolio. Want to do a room layout? \
	                       Use the tiles in your Portfolio to experiment with different combinations."
		)
		
		
	    Photographer = apps.get_model('galleries', 'photographer')
	    photographer = Photographer.objects.create(name='Ryan Phillips')
		
	    Designer = apps.get_model('galleries', 'designer')
	    designer = Designer.objects.create(name='Deindre Doherty')
	    
	    Article = apps.get_model('news', 'article')
	    featured_article = Article.objects.create(
			title = 'Bath of the Month Oct 2013',
			cover = os.path.join(settings.STATIC_ROOT, 'img/initial/news/House-Beautiful-Granada-Tile-cement.png'),
			url = '',
			date = timezone.now(),
			magazine_id = 1
		)
		
	    section_image = section.images.create(
		    tile_id = 1,
		    designer_id = designer.id,
		    photographer_id = photographer.id,
		    featured_article_id = featured_article.id,
		    image = os.path.join(settings.STATIC_ROOT, 'img/initial/content/Cluny-on-bath-Granada-tile-cement.jpg')
		)
		
	    Magazine = apps.get_model('news', 'magazine')
	    magazines = Magazine.objects.bulk_create([
		    Magazine(
			    name = 'Dwell',
			    logo = os.path.join(settings.STATIC_ROOT, 'img/initial/news/Dwell-Granada-Tile-cement.png')
			),
			Magazine(
			    name = 'Marta Living',
			    logo = os.path.join(settings.STATIC_ROOT, 'img/initial/news/Martha-Living-Granada-Tile-cement.png')
			),
			Magazine(
				name = 'AD',
				logo = os.path.join(settings.STATIC_ROOT, 'img/initial/news/AD-Granada-Tile-cement.png')
			),
			Magazine(
			    name = 'Elle Decor',
			    logo = os.path.join(settings.STATIC_ROOT, 'img/initial/news/Elle-Decor-Granada-Tile-cement.png')
			),
		])
		
	    section_image.articles.create(
			    title = '',
			    description = '',
			    url = 'http://www.dwell.com/',
			    magazine_id = 1,
			    date = timezone.now()
		)
		
	    section_image.articles.create(
			    title = '',
			    description = '',
			    url = 'http://www.coastalliving.com/',
			    magazine_id = 2,
			    date = timezone.now()
		)
	    
	    section_image.articles.create(
			    title = '',
			    description = '',
			    url = 'http://www.revistaad.es/',
			    magazine_id = 3,
			    date = timezone.now()
		)
			
	    section_image.articles.create(
			    title = '',
			    description = '',
			    url = 'http://www.elledecor.com/',
			    magazine_id = 4,
			    date = timezone.now()
		)
	

class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_auto_20150922_1944'),
    ]

    operations = [
		migrations.RunPython(addInitialData)
    ]
