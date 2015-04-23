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

ENGLISH_MISHAP = 'for casualty count check'
TAGALOG_MISHAP = 'for casualty count check'
TAGALOG_NUM = 'for casualty count check'
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
					if 'float' in str(type(i.get(x))):
						row_list.append(i.get(x))
					else:
						row_list.append(i.get(x).encode('utf-8'))
				else:
					row_list.append(' ')
			csvfile.writerow(row_list)
	print 'csv creation successful'

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
		return ' '

def open_keywords(path):
	'''
	open keyword from a local and return a list.
	'''
	with open(path, 'r') as outfile:
		keyword_list = outfile.read().splitlines()

		if '' in keyword_list:
			keyword_list.remove('')

	return keyword_list

def remove_item(json_input_list,word):
	'''
	remove dict items that has the input word in one of its keys.
	'''
	filtered_result = []
	for i in json_input_list:
		hit = 0
		for x in i.keys():
			if word in str(i.get(x, ' ')).lower():
				hit = 1

		if hit == 0:
			filtered_result.append(i)

	return filtered_result

def accident_check(s,english_keywords,tagalog_keywords,tagalog_num):
	'''
	checks the number of people involved in an accident.
	'''
	tokenizer = RegexpTokenizer(r'\w+')
	subject_words = tokenizer.tokenize(s)
	subject_words = [x.lower() for x in subject_words]

	accident_count_list = []

	for i in english_keywords:
		if i in subject_words:
			hit = 0
			rev_subject_words = subject_words[::-1]
			word_index = rev_subject_words.index(i)

			try:
				rev_subject_words = rev_subject_words[word_index+1:]
			except IndexError:
				break
			for x in rev_subject_words:
				try:
					accident_count = int(x)
					accident_count_list.append((i,accident_count))
					hit = 1
				except ValueError:
					pass
				if x in english_keywords:
					if hit == 0:
						accident_count_list.append((i,1))
					break
			if hit == 0:
				accident_count_list.append((i,1))

	for i in tagalog_keywords:
		if i in subject_words:
			hit = 0
			rev_subject_words = subject_words[::-1]
			word_index = rev_subject_words.index(i)
			try:
				rev_subject_words = rev_subject_words[word_index+1:]
			except IndexError:
				break
			for x in rev_subject_words:
				try:
					accident_count = int(x)
					accident_count_list.append((i,accident_count))
					hit = 1
				except ValueError:
					pass
				if x in tagalog_num.keys():
					accident_count_list.append((i,tagalog_num.get(x)))
				if x in tagalog_keywords:
					if hit == 0:
						accident_count_list.append((i,1))
						hit = 1
					break
			if hit == 0:
				accident_count_list.append((i,1))
				hit = 1

	result_string = ''
	if accident_count_list:
		for i in set(accident_count_list):
			result_string = result_string + "{0}:{1} ".format(i[0],i[1])

	return result_string

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

	common_english_words = open_keywords(COMMON_ENGLISH_WORDS_PATH)
	for i in json_list:
		i['language'] = language_check(i.get('article', ' '),common_english_words)

	json_list = remove_item(json_list,'reuter')

	for i in json_list:
		i['accident count'] = accident_check(i.get('title',' '),ENGLISH_MISHAP,TAGALOG_MISHAP,TAGALOG_NUM)

	create_csv(json_list, CSV_OUTPUT_PATH)

