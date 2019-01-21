import pandas as pd
import numpy as np
import json
from copy import copy
import pudb

data = pd.read_csv('predicted_nmf_text.txt', sep=" ", header=None)
print("Copy started")
data_new = copy(data)


def function(elem):
	return elem[1]

print()
# order_df={}
for index,each_user in data.iterrows():
	print(str(index)+"/"+str(data.shape[0]), end="\r")
	order = [(i, each_user[i]) for i in range(data.shape[1])]
	order.sort(key=function)
	order_mod = [(i, order[i][0]) for i in range(len(order))]
	final_order_ord = [(i[1]) for i in order_mod]
	# order_mod.sort(key=function)
	# final_order = [(i[0]) for i in order_mod]
	data_new.loc[index] = final_order_ord
	# pu.db


data_new.to_csv("borda_scores_order.csv", index = False)

"""
	if str(final_order) in order_df:
		order_df[str(final_order)]+=1
	else:
		order_df[str(final_order)] = 1

f = open("count.json", "w")
json.dump(order_df, f)
f.close()
"""