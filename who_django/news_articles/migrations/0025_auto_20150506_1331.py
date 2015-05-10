# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0024_auto_20150506_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='vehicle_type',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='vehicle_type_others',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
