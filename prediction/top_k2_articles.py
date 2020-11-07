import numpy as np
import json

data: np.ndarray = np.loadtxt("predicted_nmf_text.txt")
sum_scores = np.sum(data, axis=0)
print(sum_scores)

sum_scores = np.array([(x, val) for x, val in enumerate(sum_scores)])
sum_scores = sorted(sum_scores, key=lambda x: x[1], reverse=True)

data_dict = {int(k): v for k,v in sum_scores}
json.dump(data_dict, open("score_aggregate_ordering.json", 'w'))

print(data_dict)
