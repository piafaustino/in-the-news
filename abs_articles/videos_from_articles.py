'''
To sort out the video entries from the articles as they are by default
compiled in one big archive list.
'''
import json

DIRECTORY_PATH = './allpages_region.json'
ARTICLE_FILE = './allpages_article_region.json'
VIDEO_FILE = './allpages_video_region.json'

def video_from_article(directory_path, article_file, video_file):
    with open(DIRECTORY_PATH, 'r') as f:
        json_entries = [dict(t) for t in set([tuple(d.items()) for d in json.load(f)])]

    article_list = []
    video_list = []
    for n, i in enumerate(json_entries):
        if '2014' in i['byline']:
            if 'video' in i['link']:
                video_list.append(i)
            else:
                article_list.append(i)

    with open(ARTICLE_FILE, 'w') as outfile:
        json.dump(article_list, outfile)

    with open(VIDEO_FILE, 'w') as outfile:
        json.dump(video_list, outfile)

if __name__ == "__main__":
    video_from_article(DIRECTORY_PATH, ARTICLE_FILE, VIDEO_FILE)

