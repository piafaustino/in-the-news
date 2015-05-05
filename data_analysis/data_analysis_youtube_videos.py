from data_analysis import *

def uniform_date_youtube(date_string):
	try:
		date_string = date_string[:10]
	except Exception, e:
		pass
	return date_string

def link_maker_youtube(youtube_id):
	link = 'https://www.youtube.com/watch?v=' + youtube_id
	return link

if __name__ == "__main__":
	json_pathnames = [os.path.join(DIRECTORY_PATH, i) for i in os.listdir(DIRECTORY_PATH)]
	json_list = []
	for i in json_pathnames:
		json_file = json_loader(i)
		json_list.extend(json_file)

	for i in json_list:
		if 'abs-cbnnews' in i['description'].lower():
			i['source'] = 'abs-cbnnews'
		elif 'gma' in i['description'].lower():
			i['source'] = 'gmanetwork'
		elif 'inquirer' in i['description'].lower():
			i['source'] = 'inquirer'

	for i in json_list:
		title = i['title']
		i['relevance ranking'] = relevance_ranking(title,ENGLISH_KEYWORDS,ENGLISH_KEYWORDS_2ND,TAGALOG_KEYWORDS)

	common_english_words = open_keywords(COMMON_ENGLISH_WORDS_PATH)
	for i in json_list:
		i['language'] = language_check(i.get('title', ' '),common_english_words)

	for i in json_list:
		i['accident count'] = accident_check(i.get('title',' '),ENGLISH_MISHAP,TAGALOG_MISHAP,TAGALOG_NUM)

	#to get a standard year-month-day date.
	for i in json_list:
		i['date'] = uniform_date_youtube(i.get('publishedAt',''))

	#to get a link:
	for i in json_list:
		i['link'] = link_maker_youtube(i.get('id',''))

	#to create a csv_file.
	create_csv(json_list, CSV_OUTPUT_PATH)

	#to create a json file.
	with open(JSON_OUTPUT_PATH, 'w') as outfile:
		json.dump(json_list, outfile)
		print "json file creation complete"
