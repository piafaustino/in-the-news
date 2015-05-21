# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0032_auto_20150518_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='road_crash_liable',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
