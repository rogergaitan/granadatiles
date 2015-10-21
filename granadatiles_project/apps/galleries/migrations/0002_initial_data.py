# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.db import models, migrations
from django.conf import settings

def addInitialData(apps, schema_editor):
   if settings.DEBUG == True:
        Gallery = apps.get_model('galleries', 'gallery')
        GalleryCategory = apps.get_model('galleries', 'gallerycategory')
        GalleryImage = apps.get_model('galleries', 'GalleryImage')
        Gallery.objects.bulk_create([
           Gallery(
               name='Residential Cement Tile',
               image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/Installation-Residential-Cement-Tile-Granada-Tile-Cement.jpg'),
           ),
                   
           Gallery(
               name='Commercial Cement Tile',
               image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/Installation-Commercial-Cement-Tile-Granada-Tile-Cement.jpg'),
           ),  
                  
           Gallery(
               name='Collection',
               image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/Installation-Collection-Cement-Tile-Granada-Tile-Cement.jpg'),
           ),  
           
           Gallery(
               name='United States Cities',
               image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/Installation-United-States-Cement-Tile-Granada-Tile-Cement.jpg'),
           ),
                   
           Gallery(
               name='Historic Tile Installations',
               image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/Installation-Historic-Tiles-Cement-Tile-Granada-Tile-Cement.jpg'),
           
          )
        
        ])
                   
        GalleryCategory.objects.bulk_create([
           GalleryCategory(
               name='Kitchen',
               gallery_id=1
           ),
                   
           GalleryCategory(
               name='Bathroom',
               gallery_id=1
           ),
                   
           GalleryCategory(
               name='Living Room',
               gallery_id=1
           ),
                   
           GalleryCategory(
               name='Outdoors',
               gallery_id=1
           ),
      
           GalleryCategory(
               name='Restaurant',
               gallery_id=2
           ),
                   
           GalleryCategory(
               name='Cafe',
               gallery_id=2
           ),
                   
           GalleryCategory(
               name='Resort & Hotel',
               gallery_id=2
           ),
                   
           GalleryCategory(
               name='Retail Office',
               gallery_id=2
           ),
           
           GalleryCategory(
               name='Echo Tile Collection',
               gallery_id=3
           ),
                   
           GalleryCategory(
               name='Minis Tile Collection',
               gallery_id=3
           ),
                   
           GalleryCategory(
               name='Mauresque Tile Collection',
               gallery_id=3
           ),
           
           GalleryCategory(
               name='Chicago',
               gallery_id=4
           ),
                   
           GalleryCategory(
               name='Los Angeles',
               gallery_id=4
           ),
           
           GalleryCategory(
               name='America',
               gallery_id=5
           ),
                   
           GalleryCategory(
               name='Europe',
               gallery_id=5
           ),
                   
           GalleryCategory(
               name='Asia',
               gallery_id=5
           ),
        ])

        GalleryImage.objects.bulk_create([
            GalleryImage(
                title='Vivamus quis mi',
                description='Proin magna. Sed fringilla mauris sit amet nibh. Vivamus aliquet elit ac nisl.\
                            Proin pretium, leo ac pellentesque mollis, felis nunc ultrices eros, sed gravida\
                            augue augue mollis justo. Pellentesque posuere. Vestibulum dapibus nunc ac augue.\
                            Nulla sit amet est. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis,\
                            ipsum. Phasellus dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices\
                            posuere cubilia Curae; Fusce id purus.',
                image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/categories/residential/bathroom.jpg'),
                galleryCategory_id=2
            ),
            GalleryImage(
                title='Vivamus quis mi',
                description='Proin magna. Sed fringilla mauris sit amet nibh. Vivamus aliquet elit ac nisl.\
                            Proin pretium, leo ac pellentesque mollis, felis nunc ultrices eros, sed gravida\
                            augue augue mollis justo. Pellentesque posuere. Vestibulum dapibus nunc ac augue.\
                            Nulla sit amet est. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis,\
                            ipsum. Phasellus dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices\
                            posuere cubilia Curae; Fusce id purus.',
                image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/categories/residential/dinningroom.jpg'),
                galleryCategory_id=3
            ),
            GalleryImage(
                title='Vivamus quis mi',
                description='Proin magna. Sed fringilla mauris sit amet nibh. Vivamus aliquet elit ac nisl.\
                            Proin pretium, leo ac pellentesque mollis, felis nunc ultrices eros, sed gravida\
                            augue augue mollis justo. Pellentesque posuere. Vestibulum dapibus nunc ac augue.\
                            Nulla sit amet est. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis,\
                            ipsum. Phasellus dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices\
                            posuere cubilia Curae; Fusce id purus.',
                image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/categories/residential/outdoor.jpg'),
                galleryCategory_id=4
            ),
            GalleryImage(
                title='Vivamus quis mi',
                description='Proin magna. Sed fringilla mauris sit amet nibh. Vivamus aliquet elit ac nisl.\
                            Proin pretium, leo ac pellentesque mollis, felis nunc ultrices eros, sed gravida\
                            augue augue mollis justo. Pellentesque posuere. Vestibulum dapibus nunc ac augue.\
                            Nulla sit amet est. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis,\
                            ipsum. Phasellus dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices\
                            posuere cubilia Curae; Fusce id purus.',
                image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/categories/comercial/restorant.jpg'),
                galleryCategory_id=5
            ),
            GalleryImage(
                title='Vivamus quis mi',
                description='Proin magna. Sed fringilla mauris sit amet nibh. Vivamus aliquet elit ac nisl.\
                            Proin pretium, leo ac pellentesque mollis, felis nunc ultrices eros, sed gravida\
                            augue augue mollis justo. Pellentesque posuere. Vestibulum dapibus nunc ac augue.\
                            Nulla sit amet est. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis,\
                            ipsum. Phasellus dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices\
                            posuere cubilia Curae; Fusce id purus.',
                image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/categories/comercial/cafe.jpg'),
                galleryCategory_id=6
            ),
            GalleryImage(
                title='Vivamus quis mi',
                description='Proin magna. Sed fringilla mauris sit amet nibh. Vivamus aliquet elit ac nisl.\
                            Proin pretium, leo ac pellentesque mollis, felis nunc ultrices eros, sed gravida\
                            augue augue mollis justo. Pellentesque posuere. Vestibulum dapibus nunc ac augue.\
                            Nulla sit amet est. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis,\
                            ipsum. Phasellus dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices\
                            posuere cubilia Curae; Fusce id purus.',
                image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/categories/comercial/hotel.jpg'),
                galleryCategory_id=7
            ),
            GalleryImage(
                title='Vivamus quis mi',
                description='Proin magna. Sed fringilla mauris sit amet nibh. Vivamus aliquet elit ac nisl.\
                            Proin pretium, leo ac pellentesque mollis, felis nunc ultrices eros, sed gravida\
                            augue augue mollis justo. Pellentesque posuere. Vestibulum dapibus nunc ac augue.\
                            Nulla sit amet est. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis,\
                            ipsum. Phasellus dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices\
                            posuere cubilia Curae; Fusce id purus.',
                image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/categories/comercial/office.jpg'),
                galleryCategory_id=8
            ),
            GalleryImage(
                title='Vivamus quis mi',
                description='Proin magna. Sed fringilla mauris sit amet nibh. Vivamus aliquet elit ac nisl.\
                            Proin pretium, leo ac pellentesque mollis, felis nunc ultrices eros, sed gravida\
                            augue augue mollis justo. Pellentesque posuere. Vestibulum dapibus nunc ac augue.\
                            Nulla sit amet est. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis,\
                            ipsum. Phasellus dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices\
                            posuere cubilia Curae; Fusce id purus.',
                image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/categories/collection/echo.jpg'),
                galleryCategory_id=9
            ),
            GalleryImage(
                title='Vivamus quis mi',
                description='Proin magna. Sed fringilla mauris sit amet nibh. Vivamus aliquet elit ac nisl.\
                            Proin pretium, leo ac pellentesque mollis, felis nunc ultrices eros, sed gravida\
                            augue augue mollis justo. Pellentesque posuere. Vestibulum dapibus nunc ac augue.\
                            Nulla sit amet est. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis,\
                            ipsum. Phasellus dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices\
                            posuere cubilia Curae; Fusce id purus.',
                image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/categories/collection/minis.jpg'),
                galleryCategory_id=10
            ),
            GalleryImage(
                title='Vivamus quis mi',
                description='Proin magna. Sed fringilla mauris sit amet nibh. Vivamus aliquet elit ac nisl.\
                            Proin pretium, leo ac pellentesque mollis, felis nunc ultrices eros, sed gravida\
                            augue augue mollis justo. Pellentesque posuere. Vestibulum dapibus nunc ac augue.\
                            Nulla sit amet est. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis,\
                            ipsum. Phasellus dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices\
                            posuere cubilia Curae; Fusce id purus.',
                image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/categories/collection/mauresque.jpg'),
                galleryCategory_id=11
            ),
            GalleryImage(
                title='Vivamus quis mi',
                description='Proin magna. Sed fringilla mauris sit amet nibh. Vivamus aliquet elit ac nisl.\
                            Proin pretium, leo ac pellentesque mollis, felis nunc ultrices eros, sed gravida\
                            augue augue mollis justo. Pellentesque posuere. Vestibulum dapibus nunc ac augue.\
                            Nulla sit amet est. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis,\
                            ipsum. Phasellus dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices\
                            posuere cubilia Curae; Fusce id purus.',
                image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/categories/city/losangeles.jpg'),
                galleryCategory_id=12
            ),
            GalleryImage(
                title='Vivamus quis mi',
                description='Proin magna. Sed fringilla mauris sit amet nibh. Vivamus aliquet elit ac nisl.\
                            Proin pretium, leo ac pellentesque mollis, felis nunc ultrices eros, sed gravida\
                            augue augue mollis justo. Pellentesque posuere. Vestibulum dapibus nunc ac augue.\
                            Nulla sit amet est. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis,\
                            ipsum. Phasellus dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices\
                            posuere cubilia Curae; Fusce id purus.',
                image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/categories/city/miami.jpg'),
                galleryCategory_id=13
            ),
            GalleryImage(
                title='Vivamus quis mi',
                description='Proin magna. Sed fringilla mauris sit amet nibh. Vivamus aliquet elit ac nisl.\
                            Proin pretium, leo ac pellentesque mollis, felis nunc ultrices eros, sed gravida\
                            augue augue mollis justo. Pellentesque posuere. Vestibulum dapibus nunc ac augue.\
                            Nulla sit amet est. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis,\
                            ipsum. Phasellus dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices\
                            posuere cubilia Curae; Fusce id purus.',
                image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/categories/historic/america.jpg'),
                galleryCategory_id=14
            ),
            GalleryImage(
                title='Vivamus quis mi',
                description='Proin magna. Sed fringilla mauris sit amet nibh. Vivamus aliquet elit ac nisl.\
                            Proin pretium, leo ac pellentesque mollis, felis nunc ultrices eros, sed gravida\
                            augue augue mollis justo. Pellentesque posuere. Vestibulum dapibus nunc ac augue.\
                            Nulla sit amet est. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis,\
                            ipsum. Phasellus dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices\
                            posuere cubilia Curae; Fusce id purus.',
                image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/categories/historic/europa.jpg'),
                galleryCategory_id=15
            ),
            GalleryImage(
                title='Vivamus quis mi',
                description='Proin magna. Sed fringilla mauris sit amet nibh. Vivamus aliquet elit ac nisl.\
                            Proin pretium, leo ac pellentesque mollis, felis nunc ultrices eros, sed gravida\
                            augue augue mollis justo. Pellentesque posuere. Vestibulum dapibus nunc ac augue.\
                            Nulla sit amet est. Duis arcu tortor, suscipit eget, imperdiet nec, imperdiet iaculis,\
                            ipsum. Phasellus dolor. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices\
                            posuere cubilia Curae; Fusce id purus.',
                image=os.path.join(settings.STATIC_URL,
                   'img/initial/galleries/categories/historic/asia.jpg'),
                galleryCategory_id=16
            ),
        ])




class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(addInitialData)
    ]
