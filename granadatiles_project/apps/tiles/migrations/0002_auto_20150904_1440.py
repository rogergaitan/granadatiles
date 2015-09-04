# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.utils.methods


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=160)),
                ('title_es', models.CharField(null=True, blank=True, max_length=160)),
                ('image', models.ImageField(upload_to=apps.utils.methods.model_directory_path)),
                ('description', models.TextField()),
                ('description_es', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='tile',
            name='collection',
        ),
        migrations.AddField(
            model_name='collection',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='description_es',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='image',
            field=models.ImageField(default='', upload_to=apps.utils.methods.model_directory_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='title_es',
            field=models.CharField(null=True, blank=True, max_length=160),
        ),
        migrations.AddField(
            model_name='tile',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tile',
            name='description_es',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='tile',
            name='image',
            field=models.ImageField(default='', upload_to=apps.utils.methods.model_directory_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tile',
            name='title_es',
            field=models.CharField(null=True, blank=True, max_length=160),
        ),
        migrations.AlterField(
            model_name='collection',
            name='title',
            field=models.CharField(max_length=160),
        ),
        migrations.AlterField(
            model_name='tile',
            name='title',
            field=models.CharField(max_length=160),
        ),
        migrations.AddField(
            model_name='group',
            name='collection',
            field=models.ForeignKey(to='tiles.Collection'),
        ),
        migrations.AddField(
            model_name='tile',
            name='group',
            field=models.ForeignKey(to='tiles.Group', default=''),
            preserve_default=False,
        ),
    ]
