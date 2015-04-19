from pprint import pprint
import json

#json file returned on running a spider.
JSON_FILE = './1yearpages.json'

#keywords to check if the dict entry is traffic related or not.
TRAFFIC_KEYWORDS = './keywords_and_urls/traffic_keywords'

#to append to the links scraped.
DOMAIN NAME = 'http://www.gmanetwork.com'

#filename for the output.
FILE_NAME = './keywords_and_urls/traffic_urls'

if __name__ == "__main__":
	with open(TRAFFIC_KEYWORDS, 'r') as f:
		traffic_keywords = f.read().splitlines()

	traffic_keywords_list = [x.decode('utf-8').strip().lower() for x in traffic_keywords]
	traffic_keywords_list = [' ' + keyword + ' ' for keyword in traffic_keywords_list]

	with open(JSON_FILE, 'r') as f:
		json_videos = json.loads(f)

	#to remove duplicates. Convert the dicts to tuples first so set can be used.
	json_videos = [dict(t) for t in set([tuple(d.items()) for d in json_videos])]

	traffic_video_list = []

	for video in json_videos:
		for keyword in traffic_keywords_list:
			if keyword in article['title'].lower():
				video['link'] = DOMAIN_NAME + video.get('link')
				traffic_video_list.append(video)
				break

	with open(FILE_NAME, 'w') as file:
		for video in traffic_video_list:
			file.write()
