# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0017_auto_20150429_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='commentcount',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='dislike_count',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='duration',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='favoriecount',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='likecount',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='news_type',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='publishedAt',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='viewcount',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='youtube_id',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
    ]
