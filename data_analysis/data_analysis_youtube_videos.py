from data_analysis import *

if __name__ == "__main__":
	json_pathnames = [os.path.join(DIRECTORY_PATH, i) for i in os.listdir(DIRECTORY_PATH)]
	json_list = []
	for i in json_pathnames:
		json_file = json_loader(i)
		json_list.extend(json_file)

	for i in json_list:
		if 'abs-cbnnews' in i['description'].lower():
			i['source'] = 'abs'
		elif 'gma' in i['description'].lower():
			i['source'] = 'gma'
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

	create_csv(json_list, CSV_OUTPUT_PATH)
