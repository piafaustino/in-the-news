# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0025_auto_20150506_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='order_id',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
