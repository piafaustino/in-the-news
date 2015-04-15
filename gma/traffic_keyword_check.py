from pprint import pprint
import json

#json file returned on running gma_spider.py which gets all the titles and links
#of all the articles for 6 months
JSON_FILE = './scrape_results/gma_article2014.json'

#keywords to check if the article is a traffic related or not.
TRAFFIC_KEYWORDS = './keywords_and_urls/traffic_keywords'

#to append to the links scraped if the url is not complete
DOMAIN_NAME = 'http://www.gmanetwork.com'

#filename for the output
FILE_NAME = './keywords_and_urls/traffic_urls'

def keyword_variants(punct):
	return [' ' + keyword + str(punct) for keyword in traffic_keywords_list]

if __name__ == "__main__":
	with open(TRAFFIC_KEYWORDS, 'r') as f:
		traffic_keywords = f.read().splitlines()

	traffic_keywords_list = [x.strip().lower() for x in traffic_keywords]



	traffic_keywords_list = map(keyword_variants, [' ', '.',',',':',';'])
	traffic_keywords_list = [i for l in traffic_keywords_list for i in l]

	with open(JSON_FILE, 'r') as f:
		json_articles = json.load(f)

	traffic_article_list = []

	for article in json_articles:
		for keyword in traffic_keywords_list:
			try:
				if keyword in str(article['title']).lower():
					article['link'] = DOMAIN_NAME + article.get('link')
					print article['link']
					traffic_article_list.append(article)
			except:
				break
	with open(FILE_NAME, 'w') as file:
		for article in traffic_article_list:
			file.write(article['link']+'\n')
