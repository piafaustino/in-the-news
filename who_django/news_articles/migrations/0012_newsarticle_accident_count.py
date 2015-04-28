# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0011_auto_20150428_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='accident_count',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
