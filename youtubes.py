#import json
#from urllib.request import urlopen
#url = "http://gdata.youtube.com/feeds/api/standardfeeds /top_rated?alt-json"
#response = urlopen(url)
#contents = response.read()
#text = contents.decode('utf8')
#data = json.loads(text)
#for video in data['feed'][0:6]:
#	print(video['title']['$t'])

import requests
url = "http://gdata.youtube.com/feeds/api/standardfeeds/top_rated?alt=json"
response = requests.get(url)
data = response.json()
for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])
    
#Link no longer available