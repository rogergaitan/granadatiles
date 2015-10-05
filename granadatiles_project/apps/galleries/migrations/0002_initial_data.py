# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.db import models, migrations
from django.conf import settings

def addInitialData(apps, schema_editor):
   if settings.DEBUG == True:
        Gallery = apps.get_model('galleries', 'gallery')
        GalleryCategory = apps.get_model('galleries', 'gallerycategory')
        Gallery.objects.bulk_create([
           Gallery(
               name = 'Residential Cement Tile',
               image = os.path.join(settings.STATIC_URL, 
                   'img/initial/galleries/Installation-Residential-Cement-Tile-Granada-Tile-Cement.jpg'),
           ),
                   
           Gallery(
               name = 'Commercial Cement Tile',
               image = os.path.join(settings.STATIC_URL, 
                   'img/initial/galleries/Installation-Commercial-Cement-Tile-Granada-Tile-Cement.jpg'),
           ),  
                  
           Gallery(
               name = 'Collection',
               image = os.path.join(settings.STATIC_URL, 
                   'img/initial/galleries/Installation-Collection-Cement-Tile-Granada-Tile-Cement.jpg'),
           ),  
           
           Gallery(
               name = 'United States Cities',
               image = os.path.join(settings.STATIC_URL, 
                   'img/initial/galleries/Installation-United-States-Cement-Tile-Granada-Tile-Cement.jpg'),
           ),
                   
           Gallery(
               name = 'Historic Tile Installations',
               image = os.path.join(settings.STATIC_URL, 
                   'img/initial/galleries/Installation-Historic-Tiles-Cement-Tile-Granada-Tile-Cement.jpg'),
           
          )
        
        ])
                   
        GalleryCategory.objects.bulk_create([
           GalleryCategory(
               name = 'Kitchen',
               gallery_id = 1
           ),
                   
           GalleryCategory(
               name = 'Bathroom',
               gallery_id = 1
           ),
                   
           GalleryCategory(
               name = 'Living Room',
               gallery_id = 1
           ),
                   
           GalleryCategory(
               name = 'Outdoors',
               gallery_id = 1
           ),
      
           GalleryCategory(
               name = 'Restaurant',
               gallery_id = 2
           ),
                   
           GalleryCategory(
               name = 'Cafe',
               gallery_id = 2
           ),
                   
           GalleryCategory(
               name = 'Resort & Hotel',
               gallery_id = 2
           ),
                   
           GalleryCategory(
               name = 'Retail Office',
               gallery_id = 2
           ),
           
           GalleryCategory(
               name = 'Echo Tile Collection',
               gallery_id = 3
           ),
                   
           GalleryCategory(
               name = 'Minis Tile Collection',
               gallery_id = 3
           ),
                   
           GalleryCategory(
               name = 'Mauresque Tile Collection',
               gallery_id = 3
           ),
           
           GalleryCategory(
               name = 'Chicago',
               gallery_id = 4
           ),
                   
           GalleryCategory(
               name = 'Los Angeles',
               gallery_id = 4
           ),
           
           GalleryCategory(
               name = 'America',
               gallery_id = 5
           ),
                   
           GalleryCategory(
               name = 'Europe',
               gallery_id = 5
           ),
                   
           GalleryCategory(
               name = 'Asia',
               gallery_id = 5
           ),
        ])


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(addInitialData)
    ]
