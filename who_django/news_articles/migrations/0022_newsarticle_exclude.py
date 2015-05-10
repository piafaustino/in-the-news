# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0021_auto_20150505_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='exclude',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
