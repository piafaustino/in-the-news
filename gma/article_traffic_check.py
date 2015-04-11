from pprint import pprint
from unidecode import unidecode
import json

#json file returned on running gma_spider.py which gets all the titles and links
#of all the articles for 6 months
JSON_FILE = 'allpages.json'

#keywords to check if the article is a traffic related or not.
TRAFFIC_KEYWORDS = 'traffic_keywords'


with open('traffic_keywords', 'r') as f:
	traffic_keywords = f.read().splitlines()

traffic_keywords_list = [unidecode(x.decode('utf8')).strip().lower() for x in traffic_keywords_list]
traffic_keywords_list = [' ' + keyword + ' ' for keyword in traffic_keywords_list]

with open(JSON_FILE, 'r') as f:
	json_articles = json.load(f)

traffic_article_list = []

for article in json_articles:
#	words = article['title'].lower().split()
	for keyword in traffic_keywords_list:
		if keyword in article['title'].lower():
			traffic_article_list.append(article)
			break

for article in traffic_article_list:
	link = article['link']
	article['link'] = 'http://www.gmanetwork.com' + link
	print article['link']
