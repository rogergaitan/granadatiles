# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.conf import settings
from django.db import models, migrations


def addInitialData(apps, schema_editor):
    if settings.DEBUG == True:
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
                menu_image=os.path.join(settings.STATIC_URL, 'img/initial/tiles/icon-Echo-Collection-Granada-Tile-Cement.jpg'),
                introduction='The Echo Tile Collection revitalizes an art form that developed in France in the mid-1800s\
                        and quickly spread around the world. Unlike ceramic tiles, which are usually glazed and ﬁred,\
                         decorative cement tiles are made by ﬁrst pouring a mixture of cement and color pigment into\
                          separate compartments in a metal mold.'
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
                menu_image=os.path.join(settings.STATIC_URL, 'img/initial/tiles/Icon-Minis-Collection-Granada-Tile-Cement.png'),
                introduction='Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Proin magna.\
                        Nulla neque dolor, sagittis eget, iaculis quis, molestie non, velit. Etiam sit amet orci eget\
                        eros faucibus tincidunt. Nullam quis ante.Proin viverra, ligula sit amet ultrices semper, ligula\
                        arcu tristique sapien, a accumsan nisi mauris ac eros. Vestibulum suscipit nulla quis orci.\
                        Aenean massa. Nullam nulla eros, ultricies sit amet, nonummy id, imperdiet feugiat, pede.\
                        Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'
            ),
            collection(
                title='Andalucía Tile Collection',
                title_es='',
                slug='andalucia',
                slug_es='andalucia',
                description='''<ul><li>Inspired by France and Morocco</li>
                <li>Variety of shapes and sizes</li>
                <li>Use on bathroom floors and walls, kitchen backsplashes and more</li></ul>''',
                description_es='',
                image=os.path.join(settings.STATIC_URL, 'img/initial/tiles/kitchen-minis-compressor_ca6NA4u.jpg'),
                menu_image=os.path.join(settings.STATIC_URL, 'img/initial/tiles/Icon-Mauresque-Collection-Granada-Tile-Cement.png'),
                introduction='Pellentesque libero tortor, tincidunt et, tincidunt eget, semper nec, quam. Proin magna.\
                        Nulla neque dolor, sagittis eget, iaculis quis, molestie non, velit. Etiam sit amet orci eget\
                        eros faucibus tincidunt. Nullam quis ante.Proin viverra, ligula sit amet ultrices semper, ligula\
                        arcu tristique sapien, a accumsan nisi mauris ac eros. Vestibulum suscipit nulla quis orci.\
                        Aenean massa. Nullam nulla eros, ultricies sit amet, nonummy id, imperdiet feugiat, pede.\
                        Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.'
            ),
        ])

        group = apps.get_model('tiles', 'Group')
        echo_collection = collection.objects.filter(title='Echo Tile Collection').first()
        minis_collection = collection.objects.filter(title='Minis Tile Collection').first()
        andalucia_collection = collection.objects.filter(title='Andalucía Tile Collection').first()
        group.objects.bulk_create([
            group(
                title='Essential Shapes',
                title_es='',
                slug='essential-shapes',
                slug_es='essential-shapes',
                description='Lorem ipsum dolor sit amet consectetur adipsicing',
                description_es='',
                image=os.path.join(settings.STATIC_URL,
                                   'img/initial/tiles/groups/Designer-Erin-Adams-Granada-Tile-Cement.jpg'),
                collection=echo_collection
            ),
            group(
                title='Mediterranean',
                title_es='',
                slug='mediterranean',
                slug_es='mediterranean',
                description='Lorem ipsum dolor sit amet consectetur adipsicing',
                description_es='',
                image=os.path.join(settings.STATIC_URL,
                                   'img/initial/tiles/groups/Essential-Shapes-Granada-Tile-Cement.jpg'),
                collection=echo_collection
            ),
            group(
                title='Moroccan',
                title_es='',
                slug='moroccan',
                slug_es='moroccan',
                description='Lorem ipsum dolor sit amet consectetur adipsicing',
                description_es='',
                image=os.path.join(settings.STATIC_URL,
                                   'img/initial/tiles/groups/Mediterranean-Granada-Tile-Cement.jpg'),
                collection=echo_collection
            ),
            group(
                title='Designer Erin Adams',
                title_es='',
                slug='designer-erin-adams',
                slug_es='designer-erin-adams',
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
            group(
                title='Cras ultricies',
                title_es='',
                slug='cras-ultricies',
                slug_es='cras-ultricies',
                description='Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Vivamus aliquet elit ac nisl.\
                    Vestibulum eu odio. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Vestibulum\
                    rutrum, mi nec elementum vehicula, eros quam gravida nisl, id fringilla neque ante vel mi.Pellentesque\
                    auctor neque nec urna. Ut leo. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet,\
                    leo. Fusce fermentum. Aliquam eu nunc.',
                description_es='',
                image=os.path.join(settings.STATIC_URL,
                                   'img/initial/tiles/groups/image_1.jpg'),
                collection=minis_collection
            ),
            group(
                title='Fusce ac',
                title_es='',
                slug='fusce-ac',
                slug_es='fusce-ac',
                description='Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Vivamus aliquet elit ac nisl.\
                    Vestibulum eu odio. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Vestibulum\
                    rutrum, mi nec elementum vehicula, eros quam gravida nisl, id fringilla neque ante vel mi.Pellentesque\
                    auctor neque nec urna. Ut leo. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet,\
                    leo. Fusce fermentum. Aliquam eu nunc.',
                description_es='',
                image=os.path.join(settings.STATIC_URL,
                                   'img/initial/tiles/groups/image_2.jpg'),
                collection=minis_collection
            ),
            group(
                title='Ut varius tincidunt',
                title_es='',
                slug='ut-varius-tincidunt',
                slug_es='ut-varius-tincidunt',
                description='Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Vivamus aliquet elit ac nisl.\
                    Vestibulum eu odio. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Vestibulum\
                    rutrum, mi nec elementum vehicula, eros quam gravida nisl, id fringilla neque ante vel mi.Pellentesque\
                    auctor neque nec urna. Ut leo. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet,\
                    leo. Fusce fermentum. Aliquam eu nunc.',
                description_es='',
                image=os.path.join(settings.STATIC_URL,
                                   'img/initial/tiles/groups/image_3.jpg'),
                collection=minis_collection
            ),
            group(
                title='Sed lectus',
                title_es='',
                slug='sed-lectus',
                slug_es='sed-lectus',
                description='Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Vivamus aliquet elit ac nisl.\
                    Vestibulum eu odio. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Vestibulum\
                    rutrum, mi nec elementum vehicula, eros quam gravida nisl, id fringilla neque ante vel mi.Pellentesque\
                    auctor neque nec urna. Ut leo. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet,\
                    leo. Fusce fermentum. Aliquam eu nunc.',
                description_es='',
                image=os.path.join(settings.STATIC_URL,
                                   'img/initial/tiles/groups/image_4.jpg'),
                collection=minis_collection
            ),
            group(
                title='Cras ultricies me',
                title_es='',
                slug='cras-ultricies-me',
                slug_es='cras-ultricies-me',
                description='Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Vivamus aliquet elit ac nisl.\
                    Vestibulum eu odio. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Vestibulum\
                    rutrum, mi nec elementum vehicula, eros quam gravida nisl, id fringilla neque ante vel mi.Pellentesque\
                    auctor neque nec urna. Ut leo. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet,\
                    leo. Fusce fermentum. Aliquam eu nunc.',
                description_es='',
                image=os.path.join(settings.STATIC_URL,
                                   'img/initial/tiles/groups/image_5.jpg'),
                collection=andalucia_collection
            ),
            group(
                title='Fusce acce',
                title_es='',
                slug='fusce-acce',
                slug_es='fusce-acce',
                description='Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Vivamus aliquet elit ac nisl.\
                    Vestibulum eu odio. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Vestibulum\
                    rutrum, mi nec elementum vehicula, eros quam gravida nisl, id fringilla neque ante vel mi.Pellentesque\
                    auctor neque nec urna. Ut leo. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet,\
                    leo. Fusce fermentum. Aliquam eu nunc.',
                description_es='',
                image=os.path.join(settings.STATIC_URL,
                                   'img/initial/tiles/groups/image_6.jpg'),
                collection=andalucia_collection
            ),
            group(
                title='Varius tincidunt',
                title_es='',
                slug='varius-tincidunt',
                slug_es='varius-tincidunt',
                description='Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Vivamus aliquet elit ac nisl.\
                    Vestibulum eu odio. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Vestibulum\
                    rutrum, mi nec elementum vehicula, eros quam gravida nisl, id fringilla neque ante vel mi.Pellentesque\
                    auctor neque nec urna. Ut leo. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet,\
                    leo. Fusce fermentum. Aliquam eu nunc.',
                description_es='',
                image=os.path.join(settings.STATIC_URL,
                                   'img/initial/tiles/groups/image_7.jpg'),
                collection=andalucia_collection
            ),
            group(
                title='Sed lectus ho',
                title_es='',
                slug='sed-lectus-ho',
                slug_es='sed-lectus-ho',
                description='Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Vivamus aliquet elit ac nisl.\
                    Vestibulum eu odio. Vestibulum purus quam, scelerisque ut, mollis sed, nonummy id, metus. Vestibulum\
                    rutrum, mi nec elementum vehicula, eros quam gravida nisl, id fringilla neque ante vel mi.Pellentesque\
                    auctor neque nec urna. Ut leo. Curabitur ligula sapien, tincidunt non, euismod vitae, posuere imperdiet,\
                    leo. Fusce fermentum. Aliquam eu nunc.',
                description_es='',
                image=os.path.join(settings.STATIC_URL,
                                   'img/initial/tiles/groups/image_8.jpg'),
                collection=andalucia_collection
            ),

        ])


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(addInitialData)
    ]
