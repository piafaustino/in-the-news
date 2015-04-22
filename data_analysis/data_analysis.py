from nltk.tokenize import RegexpTokenizer
from nltk.tokenize import sent_tokenize
from nltk.util import ngrams
import json
import os
import csv
import string
import re
from pprint import pprint

DIRECTORY_PATH = '<>'
CSV_OUTPUT_PATH = '<>'
COMMON_ENGLISH_WORDS_PATH = '<>'

ENGLISH_KEYWORDS = 'for relevance ranking'
ENGLISH_KEYWORDS_2ND = 'for relevance_ranking'
TAGALOG_KEYWORDS = 'for relevance_ranking'

try:
	from local_keywords_and_paths import *
except ImportError:
	pass

def relevance_ranking(s, english_keywords, english_keywords_2nd, tagalog_keywords):

	english_score = 0.0
	for i in english_keywords:
		for x in i:
			if x in s:
				english_score += 1
				break

	for i in english_keywords_2nd:
		for x in i:
			if x in s:
				english_score += 0.5
				break

	tagalog_score = 0.0
	for i in tagalog_keywords:
		for x in i:
			if x in s:
				tagalog_score += 1
				break

	return max(english_score, tagalog_score)

def json_loader(filename):
	'''
	loads a json file to a json object. Also removes duplicates.
	'''
	with open(filename, 'r') as f:
		json_entries = [dict(t) for t in set([tuple(d.items()) for d in json.load(f)])]

	return json_entries

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

		for i in json_input_list:
			row_list = []
			for x in headers:
				if i.get(x):
					row_list.append(i.get(x))
				else:
					row_list.append(' ')
			csvfile.writerow(row_list)

def language_check(s,common_english_keywords):
	'''
	Checks if the article is english or not.
	Expected input is a string, and the list of common english
	keywords.
	'''
	common_english_words = common_english_keywords
	sent_tokenize_list = sent_tokenize(s)
	first_sent = sent_tokenize_list[0]

	tokenizer = RegexpTokenizer(r'\w+')
	first_sent_words = tokenizer.tokenize(first_sent)
	first_sent_words = [x.lower() for x in first_sent_words]
	if len(set(first_sent_words).intersection(common_english_words)):
		return 'english'
	else:
		return 'tagalog'

def open_keywords(path):
	with open(path, 'r') as outfile:
		keyword_list = outfile.read().splitlines()

		if '' in keyword_list:
			keyword_list.remove('')

	return keyword_list

if __name__ == "__main__":
	json_pathnames = [os.path.join(DIRECTORY_PATH, i) for i in os.listdir(DIRECTORY_PATH)]
	json_list = []
	for i in json_pathnames:
		json_file = json_loader(i)
		json_list.extend(json_file)

	for i in json_list:
		if 'abs-cbnnews' in i['link']:
			i['source'] = 'abs-cbnnews'
		elif 'gmanetwork' in i['link']:
			i['source'] = 'gmanetwork'
		elif 'inquirer' in i['link']:
			i['source'] = 'inquirer'
		else:
			i['source'] = i['link']

	for i in json_list:
		article = ' '.join([i.get('title', ' '), i.get('article', ' ')])
		i['relevance ranking'] = relevance_ranking(article,ENGLISH_KEYWORDS,ENGLISH_KEYWORDS_2ND,TAGALOG_KEYWORDS)
		print i['relevance ranking']

	common_english_words = open_keywords(COMMON_ENGLISH_WORDS_PATH)
	for i in json_list:
		i['language'] = language_check(i.get('article', ' '),common_english_words)

	'''
	create_csv(json_list, CSV_OUTPUT)
	'''
