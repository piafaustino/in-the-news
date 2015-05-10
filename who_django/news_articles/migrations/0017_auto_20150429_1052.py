# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0016_newsarticle_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='completed',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='dominant_topic',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='larger_context',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='ongoing_coverage',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='orgs',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='potential_cause',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='report_type',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='resp_group',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='road_crash',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='road_crash_vehicles',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='solutions',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='stat_scope',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='statistics',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='tone',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='vehicle_cat',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
