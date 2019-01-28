import json
import pandas as pd
import numpy as np
import pudb

f = open("results.json", "r")
result = json.load(f)
f.close()
print("\nElection method options:")
options = {}
i = 0
for res in result:
	# pu.db
	options[str(i)] = res
	print(str(i)+": "+res)
	i+=1

method = input("\nEnter election method: ")
method = options[method]
if method=="sntv":
	K = int(input("Enter K: "))
else:
	K = len(result[method])


f = open("count.json", "r")
count = json.load(f)
f.close()

data = pd.read_csv('predicted_nmf_text.txt', sep=" ", header=None)

# pu.db

winners = set(result[method][:K])

binary_sat = 0
binary_dissat = 0

normal_sat = 0
normal_dissat = 0

sat = 0

for each in count:
	n = count[each]
	top_pref = set(json.loads(each)[:K])
	bot_pref = set(json.loads(each)[-K:])

	top_int = winners.intersection(top_pref)
	bot_int = winners.intersection(bot_pref)

	if (len(top_int)):
		binary_sat+=n
		normal_sat+=n * len(top_int)


	if (len(bot_int)):
		binary_dissat+=n
		normal_dissat+=n * len(bot_int)


normal_sat/=K
normal_dissat/=K

print("\nNormal satisfaction: "+str(normal_sat))
print("Normal dissatisfaction: "+str(normal_dissat))
print("\nBinary satisfaction: "+str(binary_sat))
print("Binary dissatisfaction: "+str(binary_dissat))

for winner in winners:
	sat+=sum(list(data[winner]))

print("\nR* satisfaction: "+str(sat))