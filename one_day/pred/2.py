import json
import pandas as pd
import numpy as np
import pudb

K = 100

def elem(a):
	return a[0][0]


f = open("results.json", "r")
text = f.read()
f.close()
result = json.loads(text)["bloc_voting_100"]
result = result[:K]
df = pd.read_csv("test.csv")
colu = df.columns.values
cols = np.delete(colu,0)

f = open("test.json", "r")
text = f.read()
f.close()
data = json.loads(text)

# f = open("../../data_small/20170101", "r")
# text = f.read()
# f.close()
# text = text.split("\n")
# original_json = json.loads(text)
# print(original_json)

f = open("../../Words/word.json", "r")
text = f.read()
f.close()
word = json.loads(text)

f = open("url2id.json", "r")
text = f.read()
f.close()
url2id = json.loads(text)

j=[]
output = []
output_list = []
# output_words = []
for i in result:
	winner = i
	# pu.db
	article_url = cols[winner]
	data_here = data[article_url]
	article_id = str(url2id[article_url])

	counter = 0
	for each_user in data_here:
		counter+=sum(data_here[each_user])
	# article_length = word[article_id]
	# print(no_of_articles)
	output.append((article_id,counter))
	# output_words.append((article_id, (counter/float(article_length)) ))
	output_list.append(article_id)
	
# for each in output:
# 	j.append([output[each],each])
# j.sort(key=elem,reverse=True)


print(output_list)
print("\n")
print(output)
print("\n")
# print(output_words)
# print(output_words)
# pu.db
count = 0
for i in range(10):
	count+=output[i][1]

print(count)
print("\n")
count = 0
for i in range(20):
	count+=output[i][1]

print(count)
print("\n")
count = 0
for i in range(100):
	count+=output[i][1]
print(count)
print("\n")