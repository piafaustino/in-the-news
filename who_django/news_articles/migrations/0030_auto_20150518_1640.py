# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0029_newsarticle_rater_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='injured_reported',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='killed_reported',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsarticle',
            name='rater_notes',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
