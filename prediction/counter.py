import pandas as pd
import numpy as np
import json

data = pd.read_csv('predicted_nmf_text_numpy.txt', sep=" ", header=None)

order_df = {}
for index, each_user in data.iterrows():
    print(f"Working for Index {index}")
    order = [(i, each_user[i]) for i in range(data.shape[1])]
    order.sort(key=lambda x: x[1], reverse=True)
    final_order = [i[0] for i in order]
    if str(final_order) in order_df:
        order_df[str(final_order)] += 1
    else:
        order_df[str(final_order)] = 1

f = open("count.json", "w")
json.dump(order_df, f)
f.close()
