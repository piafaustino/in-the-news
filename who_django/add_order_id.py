import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','who_django.settings')
import json
import django
django.setup()

from news_articles.models import NewsArticle
from pprint import pprint

text_articles = NewsArticle.objects.order_by('relevance_ranking').reverse()

count = 0
for article in text_articles:
	count += 1
	article.order_id = count
	print count, article.id
	article.save()
