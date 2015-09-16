# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_initial_social'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('title_es', models.CharField(max_length=160, blank=True, verbose_name='Title_es', null=True)),
                ('description', models.TextField(verbose_name='Description')),
                ('description_es', models.TextField(blank=True, verbose_name='Description_es', null=True)),
                ('subtitle', models.CharField(max_length=150, verbose_name='Subtitle')),
                ('subtitle_es', models.CharField(max_length=150, verbose_name='Subtitle_es')),
            ],
            options={
                'verbose_name': 'Testimony',
                'verbose_name_plural': 'Testimonials',
            },
        ),
    ]
