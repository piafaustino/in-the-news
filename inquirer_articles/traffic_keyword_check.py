from pprint import pprint
import json

#json file returned on running gma_spider.py which gets all the titles and links
#of all the articles for 6 months
JSON_FILE = './scrape_results/inquirer_articlelist_2014.json'

#keywords to check if the article is a traffic related or not.
TRAFFIC_KEYWORDS = './keywords_and_urls/traffic_keywords'

#to append to the links scraped if the url is not complete
DOMAIN_NAME = 'http://newsinfo.inquirer.net'

#filename for the output.
FILE_NAME = './keywords_and_urls/traffic_urls'

def keyword_variants(punct):
	return [' ' + keyword + str(punct) for keyword in traffic_keywords_list]


if __name__ == "__main__":
	with open(TRAFFIC_KEYWORDS, 'r') as f:
		traffic_keywords = f.read().splitlines()

	traffic_keywords_list = [x.decode('utf-8').strip().lower() for x in traffic_keywords]

	traffic_keywords_list = map(keyword_variants, [' ', '.',',',':',';'])
	traffic_keywords_list = [i for l in traffic_keywords_list for i in l]

	with open(JSON_FILE, 'r') as f:
		json_articles = json.load(f)

	#to remove duplicates. Convert the dicts to tuples first so set can be used.
	json_articles = [dict(t) for t in set([tuple(d.items()) for d in json_articles])]

	traffic_article_list = []

	for article in json_articles:
		for keyword in traffic_keywords_list:
			try:
				if keyword in article['title'].lower():
					traffic_article_list.append(article)
					print article['link']
					break
			except:
				break

	with open(FILE_NAME, 'w') as file:
		for article in traffic_article_list:
			file.write(article['link']+'\n')
