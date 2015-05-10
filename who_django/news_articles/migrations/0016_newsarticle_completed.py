# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0015_newsarticle_report_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='completed',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
    ]
