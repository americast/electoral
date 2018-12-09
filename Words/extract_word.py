import os
import json
import sys

DATA_PATH = "../data_small"

DATA_PATH2 = "home/lemeiz/content_refine/"

files = os.listdir(DATA_PATH)
count=0
# print(files)
files2 = os.listdir(DATA_PATH2)

word_dict = {}
for file in files:
	print(file)
	f = open(DATA_PATH+"/"+file).read()
	fs = f.split("\n")
	for eachf in fs:
		try:
			data = json.loads(eachf)
		except:
			pass
		if "id" in data:
			# print(data["id"])
			count+=1
			if data["id"] in files2:
				file2 = data["id"]
				f2 = open(DATA_PATH2+"/"+file2).read()
				try:
					data2 = json.loads(f2)
				except:
					pass
				article = data2["fields"][4]["value"]
				counter = 0
				for each_line in article:
					counter+=len(each_line.split())
				# print(data2["fields"][4]["value"])
				word_dict[file2] = counter
print(word_dict)
f_word = open("word.json", "w")
json.dump(word_dict,f_word)
f_word.close()
