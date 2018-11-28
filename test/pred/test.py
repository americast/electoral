import json
import pandas as pd
import pudb

f = open('test.json')
data = json.load(f)

dict_avg = {}

for each_url in data:
	dict_avg[each_url] = {}
	count = 0
	url_sum = 0
	for each_user in data[each_url]:
		local_sum = 0
		for each_time in data[each_url][each_user]:
			local_sum+=each_time
		count+=1
		url_sum+=local_sum
	url_avg = float(url_sum) / count

	for each_user in data[each_url]:
		local_sum = 0
		for each_time in data[each_url][each_user]:
			local_sum+=each_time
		dict_avg[each_url][each_user] = float(local_sum) / url_avg

	max_id = max(dict_avg[each_url], key=dict_avg[each_url].get)
	min_id = min(dict_avg[each_url], key=dict_avg[each_url].get)
	# print(dict_avg[each_url][max_value],dict_avg[each_url][min_value])
	max_value = dict_avg[each_url][max_id]
	min_value = dict_avg[each_url][min_id]
	
	for each_user in data[each_url]:
		if max_value==min_value:
			dict_avg[each_url][each_user] = 5
		else:
			temp = dict_avg[each_url][each_user]
			dict_avg[each_url][each_user] = 1 + 9 * ((temp - min_value)/(max_value - min_value))

df = pd.DataFrame(data=dict_avg)
df.to_csv("test.csv",index=False)