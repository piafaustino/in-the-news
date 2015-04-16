from pprint import pprint
import json

#json file returned on running a spider.
JSON_FILE = './scrape_results/gma_videolist_y2014.json'

#keywords to check if the dict entry is traffic related or not.
TRAFFIC_KEYWORDS = './keywords_and_urls/traffic_keywords'

#to append to the links scraped.
DOMAIN_NAME = 'http://www.gmanetwork.com'

#filename for the output.
FILE_NAME = './keywords_and_urls/traffic_urls'

#filename for the json output.
JSON_FILE_NAME = './scrape_results/gma_video_content_2014.json'

if __name__ == "__main__":
	with open(TRAFFIC_KEYWORDS, 'r') as f:
		traffic_keywords = [x.decode('utf-8').strip().lower() for x in f.read().splitlines()]

	punctuation_list = [' ', '.', ',',':',';']
	keywords = []
	for keyword in traffic_keywords_list:
		for punct in punctuation_list:
			keywords.append(' ' + keyword + punct)

	traffic_keywords_list.extend(keywords)

	with open(JSON_FILE, 'r') as f:
		json_videos = json.load(f)

	#to remove duplicates. Convert the dicts to tuples first so set can be used.
	json_videos = [dict(t) for t in set([tuple(d.items()) for d in json_videos])]

	traffic_video_list = []

	for video in json_videos:
		for keyword in traffic_keywords_list:
			if keyword in video.get('title', default=' ').lower():
				video['link'] = DOMAIN_NAME + video.get('link')
				print video['link']
				traffic_video_list.append(video)
				break

	with open(FILE_NAME, 'w') as outfile:
		for video in traffic_video_list:
			outfile.write(video['link']+'\n')

	with open(JSON_FILE_NAME, 'w') as outfile:
		json.dump(traffic_video_list, outfile)
