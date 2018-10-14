import os
import json

DATA_PATH = "data_small"

files = os.listdir(DATA_PATH)

for file in files:
	f = open(DATA_PATH+"/"+file).read()
	fs = f.split("\n")
	for eachf in fs:
		data = json.loads(eachf)
		
		print(data)