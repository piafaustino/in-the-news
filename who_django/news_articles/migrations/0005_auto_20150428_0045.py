# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0004_auto_20150428_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='kicker',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
