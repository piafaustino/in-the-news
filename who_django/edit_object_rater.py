import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','who_django.settings')
import json
import django
django.setup()

from news_articles.models import NewsArticle
from pprint import pprint

text_articles = NewsArticle.objects.filter(news_type__startswith='text')\
				.order_by('relevance_ranking').reverse()

text_mavie_articles = text_articles[:300]
text_candice_articles = text_articles[300:600]
text_pia_articles = text_articles[600:900]

count = 0
for article in text_mavie_articles:
	count += 1
	article.rater = u'mavie'
	print count, article.id, article.rater
	article.save()

for article in text_candice_articles:
	count += 1
	article.rater = u'candice'
	print count, article.id, article.rater
	article.save()

for article in text_pia_articles:
	count += 1
	article.rater = u'pia'
	print count, article.id, article.rater
	article.save()



