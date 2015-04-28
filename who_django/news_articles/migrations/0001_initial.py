# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=300)),
                ('relevance_ranking', models.FloatField()),
                ('date', models.DateField(null=True, blank=True)),
                ('source', models.CharField(max_length=20)),
                ('link', models.CharField(max_length=300)),
                ('article', models.TextField()),
                ('author', models.CharField(max_length=200, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('byline', models.CharField(max_length=200, null=True)),
                ('language', models.CharField(max_length=20, null=True)),
                ('kicker', models.CharField(max_length=200, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
