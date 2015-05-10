# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0013_auto_20150429_0335'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='road_crash_vehicles',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
    ]
