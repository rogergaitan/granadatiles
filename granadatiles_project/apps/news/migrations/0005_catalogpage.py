# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_article_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', sorl.thumbnail.fields.ImageField(verbose_name='Image', upload_to='Catalogs/Pages')),
                ('catalog', models.ForeignKey(to='news.Catalog', verbose_name='Catalog', related_name='pages')),
            ],
            options={
                'verbose_name_plural': 'Catalog Pages',
                'verbose_name': 'Catalog Page',
            },
        ),
    ]
