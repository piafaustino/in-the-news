import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','who_django.settings')
import json
import django
django.setup()
import time
from news_articles.models import NewsArticle

def json_loader(filename):
	'''
	loads a json file to a json object. Also removes duplicates and spaces.
	'''
	with open(filename, 'r') as f:
		json_entries = [dict(t) for t in set([tuple(d.items()) for d in json.load(f)])]

	return json_entries

def add_article(title, relevance_ranking, date, source, link, article='',
			    author='', location='',accident_count='',byline='',language='',kicker=''):

	n = NewsArticle.objects.get_or_create(title=title,
										  relevance_ranking=relevance_ranking,\
										  date=date,
										  source=source,
										  link=link,
										  author=author,
										  article=article,
										  location=location,
										  accident_count=accident_count,
										  byline=byline,
										  language=language,
										  kicker=kicker
										  )[0]
	n.save()
	return n

def populate(json_entries):
	count = 0

	for e in json_entries:
		'''
		try:
			strptime(e.get('date'))
		except:
			e['date'] = None
		'''
		try:
			a =	add_article(title=e.get('title', '').strip(),
						relevance_ranking=e.get('relevance ranking'),
						date=e.get('date'),
						source=e.get('source',''),
						link=e.get('link',''),
						article=e.get('article',''),
						author=e.get('author',''),
						location=e.get('location',''),
						accident_count=e.get('accident count',''),
						byline=e.get('byline',''),
						language=e.get('language',''),
						kicker=e.get('kicker','')
							)
		except Exception, e:
			count += 1
			print count, e
			continue
		print a.relevance_ranking, a.date

if __name__ == "__main__":
	json_entries = json_loader('./traffic_articles_2014_04272015_v3.json')
	populate(json_entries)

