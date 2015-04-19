from pprint import pprint
import json

#json file returned on running gma_spider.py which gets all the titles and links
#of all the articles for 6 months
JSON_FILE = './325pages.json'

#keywords to check if the article is a traffic related or not.
TRAFFIC_KEYWORDS = './keywords_and_urls/traffic_keywords'

#to append to the links scraped.
DOMAIN_NAME = 'http://www.abs-cbnnews.com'

#filename for the output.
FILE_NAME = './keywords_and_urls/traffic_urls'

if __name__ == "__main__":
	with open(TRAFFIC_KEYWORDS, 'r') as f:
		traffic_keywords = [x.decode('utf-8').strip().lower() for x in f.read().splitlines()]

	punctuation_list = [' ', '.', ',',':',';']
	keywords = []
	for keyword in traffic_keywords_list:
		for punct in punctuation_list:
			keywords.append(' ' + keyword + punct)

	traffic_keywords_list.extend(keywords)

	with open(JSON_FILE, 'r') as f:
		json_articles = json.load(f)

	#to remove duplicates. Convert the dicts to tuples first so set can be used.
	json_articles = [dict(t) for t in set([tuple(d.items()) for d in json_articles])]


	for article in json_articles:
		for keyword in traffic_keywords_list:
			if keyword in article.get('title', default= ' ').lower():
				traffic_article_list.append(article)
				break

	with open(FILE_NAME, 'w') as file:
		for article in traffic_article_list:
			link = article['link']
			article['link'] = DOMAIN_NAME + link
			file.write(article['link'])
