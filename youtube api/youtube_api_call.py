import requests
from pprint import pprint
import json
import csv

JSON_OUTPUT = '<path to json output>'
CSV_OUTPUT = '<path to csv output>'

channel_params = {
			'key':'<secret key installed applications>',
			'forUsername':'<channel name>',
			'part':'<snippet or id>'
}

search_params = {
			'key':'<secret key installed applications>',
			'part':'<snippet or id>',
			'channelId':'<channel id>',
			'maxResults':'<1 to 50>',
			'pageToken':'<from nextPageToken response>',
			'publishedAfter':'<rfc3339 formated date-time value>',
			'publishedBefore':'<rfc3339 formated date-time value>'
}

video_params = {
			'key':'<secret key installed applications>',
			'part':'<snippet,contentDetails,statistics,status>',
			'id':'<videoid>',
}

try:
	from local_params import *
except ImportError:
	pass

CHANNEL_URL = 'https://www.googleapis.com/youtube/v3/channels'
SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'
VIDEO_URL = 'https://www.googleapis.com/youtube/v3/videos'

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
					row_list.append(i.get(x).encode('utf-8'))
				else:
					row_list.append(' ')
			csvfile.writerow(row_list)
	print 'csv creation success!'

if __name__ == "__main__":
	#to get the channel id from the channel name
	r = requests.get(CHANNEL_URL, params=channel_params)
	channel_json = r.json()
	channel_ID = channel_json.get('items')[0].get('id')

	search_params['channelId'] = channel_ID
	#to remove key values that are as of the moment, empty. API will not return
	#a 200 response if not done.
	search_params = dict((k,v) for k, v in search_params.iteritems() if v)

	#to get all the video ids of the channel.
	video_id_list = []
	while True:
		r = requests.get(SEARCH_URL, params=search_params)
		search_json = r.json()

		for i in search_json.get('items'):
			videoId = i.get('id').get('videoId')
			video_id_list.append(videoId)
			print videoId

		pageToken = search_json.get('nextPageToken')
		if not pageToken:
			break
		search_params['pageToken'] = pageToken

	#to get the details of all the videoes.
	video_list = []
	for i in video_id_list:
		video_params['id'] = i
		r = requests.get(VIDEO_URL, params=video_params)
		video_json = r.json()
		try:
			items_json = video_json.get('items')[0]
			pprint(items_json)
			video_dict = {}
			video_dict['id'] = items_json.get('id')
			video_dict['title'] = items_json.get('snippet').get('title')
			video_dict['description'] = items_json.get('snippet').get('description')
			video_dict['publishedAt'] = items_json.get('snippet').get('publishedAt')
			video_dict['duration'] = items_json.get('contentDetails').get('duration')

			video_dict.update(items_json.get('statistics'))

			video_list.append(video_dict)
		except TypeError:
			continue

	with open(JSON_OUTPUT, 'w') as outfile:
		json.dump(video_list, outfile)
		print 'json creation success!'

	create_csv(video_list, CSV_OUTPUT)
