from pprint import pprint
from unidecode import unidecode
import json

with open('traffic_keywords', 'r') as f:
	traffic_keywords = f.read()

traffic_keywords_list = traffic_keywords.split('\n')
traffic_keywords_list = [unidecode(x.decode('utf8')).strip().lower() for x in traffic_keywords_list]


with open('1page.json', 'r') as f:
	json_articles = json.load(f)

traffic_article_list = []

for article in json_articles:
	words = article['title'].lower().split()

	for word in words:
		if word in traffic_keywords_list:
			traffic_article_list.append(article)
			break