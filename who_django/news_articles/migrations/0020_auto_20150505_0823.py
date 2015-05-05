# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0019_auto_20150505_0815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsarticle',
            old_name='favorie_count',
            new_name='favorite_count',
        ),
    ]
