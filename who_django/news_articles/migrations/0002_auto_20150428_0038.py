# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='article',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='author',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='byline',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='kicker',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='language',
            field=models.CharField(default='', max_length=20, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='location',
            field=models.CharField(default='', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='title',
            field=models.CharField(max_length=300, blank=True),
            preserve_default=True,
        ),
    ]
