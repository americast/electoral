import os
import json

DATA_PATH = "data_small"

files = os.listdir(DATA_PATH)
map_user2article = {}
map_article2user = {}

for file in files:
	print "processing: "+str(file)
	f = open(DATA_PATH+"/"+file).read()
	fs = f.split("\n")
	for eachf in fs:
		try:
			data = json.loads(eachf)
		except:
			pass
		
		if "profile" not in data:
			if "userId" in data and "activeTime" in data and "url" in data:
				
				if data["userId"] not in map_user2article:
					map_user2article[data["userId"]] = {}
				if data["url"] not in map_user2article[data["userId"]]:
					map_user2article[data["userId"]][data["url"]] = []
				map_user2article[data["userId"]][data["url"]].append(data["activeTime"])

				if data["url"] not in map_article2user:
					map_article2user[data["url"]] = {}
				if data["userId"] not in map_article2user[data["url"]]:
					map_article2user[data["url"]][data["userId"]] = []
				map_article2user[data["url"]][data["userId"]].append(data["activeTime"])

f_user2article = open("user2article.json", "w")
f_article2user = open("article2user.json", "w")

f_user2article.write(json.dumps(map_user2article, indent = 4))
f_article2user.write(json.dumps(map_article2user, indent = 4))