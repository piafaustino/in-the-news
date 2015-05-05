# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_articles', '0018_auto_20150504_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsarticle',
            old_name='commentcount',
            new_name='comment_count',
        ),
        migrations.RenameField(
            model_name='newsarticle',
            old_name='favoriecount',
            new_name='favorie_count',
        ),
        migrations.RenameField(
            model_name='newsarticle',
            old_name='likecount',
            new_name='like_count',
        ),
        migrations.RenameField(
            model_name='newsarticle',
            old_name='viewcount',
            new_name='view_count',
        ),
        migrations.RemoveField(
            model_name='newsarticle',
            name='publishedAt',
        ),
    ]
