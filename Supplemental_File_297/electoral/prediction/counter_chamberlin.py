import pandas as pd
import numpy as np
import json
from copy import copy

data = pd.read_csv('predicted_nmf_text_numpy.txt', sep=" ", header=None)
print("Copy started")
data_new = copy(data)

print()
# order_df={}
for index, each_user in data.iterrows():
    print(str(index) + "/" + str(data.shape[0]), end="\r")
    order = [(i, each_user[i]) for i in range(data.shape[1])]
    order.sort(key=lambda x: x[1])
    order_mod = [(i, order[i][0]) for i in range(len(order))]
    order_mod.sort(key=lambda x: x[1])
    final_order = [(i[0]) for i in order_mod]
    data_new.loc[index] = final_order

data_new.to_csv("borda_scores.csv", index=False)


