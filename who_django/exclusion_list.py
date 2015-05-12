import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','who_django.settings')
import json
import django
django.setup()
import time
from news_articles.models import NewsArticle
from pprint import pprint

EXCLUSION_TITLE_LIST_PATH = './exclusion_title_list'

def open_text_file(path):
	'''
	opens a textfile from local, separates it per new line, and returns a list.
	'''
	with open(path, 'r') as outfile:
		text_list = outfile.read().splitlines()

		if '' in text_list:
			text_list.remove('')

	return text_list

exclusion_title_list = open_text_file(EXCLUSION_TITLE_LIST_PATH)
error_count = 0
for i in exclusion_title_list:
	try:
		article = NewsArticle.objects.get(title=i)
		article.exclude = u'Yes'
		print article
		article.save()
	except Exception, e:
		print e
		error_count += 1

print len(exclusion_title_list)
print error_count
