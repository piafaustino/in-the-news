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

def add_video_article(title, relevance_ranking, date, source, link, language='',
					  view_count='', like_count='', comment_count='', favorite_count='',
					  dislike_count='', duration='', youtube_id='',news_type='video'):
	'''
	adds video files to the django database
	'''
	n = NewsArticle.objects.get_or_create(title=title,
										  relevance_ranking=relevance_ranking,
										  date=date,
										  source=source,
										  link=link,
										  language=language,
										  view_count=view_count,
										  like_count=like_count,
										  comment_count=comment_count,
										  favorite_count=favorite_count,
										  dislike_count=dislike_count,
										  duration=duration,
										  youtube_id=youtube_id,
										  news_type=news_type
										  )[0]

	n.save()
	return n

def populate(json_entries):
	count = 0

	for e in json_entries:
		try:
			a = add_video_article(title=e.get('title').strip(),
							  	relevance_ranking=e.get('relevance ranking',''),
							  	date=e.get('date'),
								source=e.get('source',''),
								link=e.get('link',''),
								language=e.get('language',''),
								view_count=e.get('viewCount',''),
								like_count=e.get('likeCount',''),
								comment_count=e.get('commentCount',''),
								favorite_count=e.get('favoriteCount',''),
								dislike_count=e.get('dislikeCount',''),
								duration=e.get('duration'),
								youtube_id=e.get('id')
							)
		except Exception, e:
			count += 1
			print count, e
			continue
		print a.relevance_ranking, a.date
	print count

if __name__ == "__main__":
	json_entries = json_loader('./traffic_youtube_videos_2014_05042015_v4.json')
	populate(json_entries)
