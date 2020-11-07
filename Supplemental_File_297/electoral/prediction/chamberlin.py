import pandas as pd
import numpy as np
from copy import copy
import datetime

K = int(input("Enter K: "))

df = pd.read_csv("borda_scores_order.csv")

winners = []
max_pos = 0
sum_here = 0
sum_max = 0

sums = [(sum(list(df[col]))) for col in df]

winners.append(np.argmax(np.array(sums)))

col_names = df.columns.values
np_array = np.zeros(df.shape)
df_here = pd.DataFrame(np_array, range(df.shape[0]), col_names)

for i in range(1, K):
    print("\niter: " + str(i))

    # for j in winners:
    # 	df_here[str(j)] = df[str(j)]

    sum_ = 0
    winner = 0
    for col in df_here:
        print(col + "/" + str(df_here.shape[1]), end="\r")
        if int(col) in winners:
            continue
        df_here[col] = df[col]
        sum_here = sum(df_here.max(axis=1))
        if sum_here > sum_:
            winner = int(col)
            sum_ = sum_here
        df_here[col] = 0
    winners.append(winner)
    df_here[str(winner)] = df[str(winner)]

print(winners)

with open('monroe.txt', 'w') as f:
    for item in winners:
        f.write("%s\n" % str(item))
