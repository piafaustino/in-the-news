# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0008_auto_20150428_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='language',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
