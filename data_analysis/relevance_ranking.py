from nltk.tokenize import RegexpTokenizer
import json
import os
import csv
import string
import re
from pprint import pprint

DIRECTORY_PATH = './traffic_articles/'
CSV_OUTPUT = './json_and_csv_results/traffic_articles_2014_04212015.csv'

def relevance_ranking(json_input):
	roadsynonyms = ['road','roads','street','streets','highway','highways','expressway','underpass','overpass','sidewalk','flyover','flyovers']
	accidentsynonyms = ['accident','tragedy','tragedies','mishap','collision','smashup','hit and run','hit-and-run']
	killedsynonyms = ['death','dead','kills','killed','die','died','dies','fatality','fatalities','casualties','casualty','injured','injuries','injury','injures','injure','hurt','hurts','flip over','flips over','flipped over','slam','slams','slammed','fall','falls','fell','crush','crushed','crushes','hit','hits','run over','ran over','runs over']
	safesynonyms = ['safe','safety','unsafe','dangerous']
	transportsynonyms = ['transport','transportation','traffic']
	vehiclesynonyms = ['car','vehicle','vehicular','bus','motorcycle','motorbike','bicycle','bike','truck','pedicab','kuliglig','jeep','jeepney','automobile']
	personynonynms = ['driver','motorist ','passenger','cyclist','biker','pedestrian','runner','jogger','commuter','traffic enforcer','traffic constable','MMDA constable','traffic officer','MMDA officer']
	accidentcauses = ['drunk','drink','drinking','asleep','texting','speeding','swerving','error','fatigue','overtaking','lost control','lose control','brake','malfunction','bad weather','poor visibility','not paying attention']
	trafficenforcement = ['seatbelt','helmet','driver education',"driver's education","drivers' education",'defensive driving','speed limit','traffic fine','traffic fines','road fine','road fines','illegal parking','illegally parked','road sign','road signage','traffic sign','stoplight','traffic light','enforcement','regulation','violation','policy','fines','ticket','number coding','color coding','traffic scheme']

	allkeywordgroups = [roadsynonyms,accidentsynonyms,killedsynonyms,safesynonyms,transportsynonyms,vehiclesynonyms,personynonynms,accidentcauses,trafficenforcement]

	article = ' '.join([json_input.get('title', ' '), json_input.get('article', ' ')])

	score = 0
	for i in allkeywordgroups:
		for x in i:
			if x in article:
				score += 1
				break

	return score

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

		for i in json_list:
			row_list = []
			for x in headers:
				if i.get(x):
					row_list.append(i.get(x))
				else:
					row_list.append(' ')
			csvfile.writerow(row_list)


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
		i['relevance ranking'] = relevance_ranking(i)

	create_csv(json_list, CSV_OUTPUT)

