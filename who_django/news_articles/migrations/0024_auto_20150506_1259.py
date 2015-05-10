# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0023_newsarticle_rater'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='dominant_topic_others',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='orgs_others',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='potential_cause_others',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='report_type_others',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='resp_group_others',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='solutions_others',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='stat_scope_others',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='vehicle_cat_others',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
