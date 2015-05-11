# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0026_newsarticle_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='accident_time_of_day',
            field=models.CharField(max_length=300, null=True, blank=True),
            preserve_default=True,
        ),
    ]
