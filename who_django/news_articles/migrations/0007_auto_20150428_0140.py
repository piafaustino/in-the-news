# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0006_auto_20150428_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsarticle',
            name='kicker',
            field=models.CharField(max_length=1000, null=True, blank=True),
            preserve_default=True,
        ),
    ]
