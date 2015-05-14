# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0028_auto_20150511_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='rater_notes',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
