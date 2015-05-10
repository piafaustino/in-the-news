from nltk.tokenize import RegexpTokenizer
import json
import os
import csv
import string
import re

DIRECTORY_PATH = './traffic_articles/'
TRAFFIC_KEYWORDS_PATH = './keywords_and_urls/traffic_keywords'
LOCATION_KEYWORDS_PATH = './keywords_and_urls/location_keywords'
JSON_OUTPUT = './json_and_csv_results/traffic_articles_2014.json'
CSV_OUTPUT = './json_and_csv_results/traffic_articles_2014.csv'

def relevance_score(article, keywords):
	'''
	article is a string
	keywords is a set for speed of "in" lookup

	A score of 1 means every single word in the article is
	relevant. A score of .10 means that for every 10 words
	there's one relevant word in the article.
	'''

	tokenizer = RegexpTokenizer(r'\w+')
	article_words = tokenizer.tokenize(article)
	article_words = [x.lower() for x in article_words]

	if not len(article_words):
		return 0
	score = 0
	for word in article_words:
		if word in keywords:
			score += 1
	return float(score)/float(len(article_words))

def json_loader(filename):
	'''
	loads a json file to a json object. Also removes duplicates.
	'''
	with open(filename, 'r') as f:
		json_entries = [dict(t) for t in set([tuple(d.items()) for d in json.load(f)])]

	return json_entries

def sort_relevance(json_input_list,top=0):
	'''
	Sorts the json entries based on the relevance score.
	Returns the top number of entries. if parameter is not specified, this will just return
	a sorted dict output.
	'''
	top_relevant = []
	json_input_list = json_input_list

	if top:
		n = top
	else:
		n = len(json_input_list)

	for c in xrange(n):
		max_score = 0
		for i in json_input_list:
			if i['relevance_score'] > max_score:
				max_score = i['relevance_score']
				top_dict = i

		top_relevant.append(top_dict)
		json_input_list.remove(top_dict)

	return top_relevant

def create_csv(json_input_list,csv_name):
	'''
	Creates a csv file from a list with json objects.
	Can accomodate jagged data sets.
	'''
	with open(csv_name, "wb+") as outfile:
		csvfile = csv.writer(outfile)

		headers = []
		for i in json_input_list:
			headers.extend(i.keys())
		headers = list(set(headers))
		csvfile.writerow(headers)

		for i in json_list:
			row_list = []
			for x in headers:
				if i.get(x):
					row_list.append(i.get(x))
				else:
					row_list.append(' ')
			csvfile.writerow(row_list)


def location_from_content(json_input, location_keywords_path):
	'''
	get the location from content and append the result to the dict.
	TO DO: still need to remove duplicates.
	'''
	with open(LOCATION_KEYWORDS_PATH, 'r') as outfile:
		location_keywords = outfile.read().splitlines()

		if '' in location_keywords:
			location_keywords.remove('')

	location_keywords = set([x.strip().lower() for x in location_keywords])
#	location_keywords = [' ' + x + punct for x in location_keywords for punct in ('',' ',',','.',':',';')]

	loc_tag = []

	article = str(json_input.get('article', ' ').lower())

	for location in location_keywords:
		if location in article:
			location = location.strip()
			loc_tag.append(location)

	# to remove false matches of Quezon Province to the article
	if 'quezon' in loc_tag:
		quezon_count = len(re.findall(r'quezon', article))
		quezon_city_count = len(re.findall(r'quezon city', article))

		if quezon_city_count == quezon_count:
			loc_tag.remove('quezon')

	if 'manila' in loc_tag:
		manila_count = len(re.findall(r'manila', article))
		metro_manila_count = len(re.findall(r'metro manila', article))

		if metro_manila_count == manila_count:
			loc_tag.remove('manila')

	return list(set(loc_tag)).join(', ')

if __name__ == "__main__":
	with open(TRAFFIC_KEYWORDS_PATH, 'r') as outfile:
		traffic_keywords = [x.decode('utf-8').strip().lower() for x in outfile.read().splitlines()]

	json_pathnames = [os.path.join(DIRECTORY_PATH,i) for i in os.listdir(DIRECTORY_PATH)]
	json_list = []
	for i in json_pathnames:
		json_file = json_loader(i)
		json_list.extend(json_file)

	#adding source per json:
	for i in json_list:
		if 'abs-cbnnews' in i['link']:
			i['source'] = 'abs-cbnnews'
		elif 'gmanetwork' in i['link']:
			i['source'] = 'gmanetwork'
		elif 'inquirer' in i['link']:
			i['source'] = 'inquirer'
		else:
			i['source'] = i['link']

	#adding relevance score to json files
	for i in json_list:
		if i['article']:
			i['relevance_score'] = relevance_score(i['article'], traffic_keywords)
		else:
			i['relevance_score'] = 0.0

'''
	count = 0
	for i in json_list:
		if location_from_content(i,LOCATION_KEYWORDS_PATH) == []:
			count += 1
	print count
'''

	#sorting with the highest relevance score
	top_relevant = sort_relevance(json_list)

	#creating a json file
	with open(JSON_OUTPUT, 'w') as outfile:
		json.dump(top_relevant, outfile)

	#part where we create csv
	create_csv(top_relevant, CSV_OUTPUT)

