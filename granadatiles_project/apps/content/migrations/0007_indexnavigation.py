# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0006_initial_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexNavigation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=150)),
                ('title_es', models.CharField(max_length=160, verbose_name='Title_es', null=True, blank=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(verbose_name='Description_es', null=True, blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=core.models.model_directory_path, verbose_name='Image')),
                ('target', models.BooleanField(help_text='Open in new tab', default=False)),
                ('link', models.URLField(verbose_name='Link', null=True, blank=True)),
                ('link_es', models.URLField(verbose_name='Link', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Index Link',
                'verbose_name_plural': 'Index Links',
            },
        ),
    ]
