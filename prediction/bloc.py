import json

f = open("count_bloc.json", "r")
input_json = json.load(f)
f.close()


def function(elem):
    return elem[1]


k = 3  # To be input
result_dict = {}
result_list = []
for each in input_json:
    count = input_json[each]
    # print("each", each)
    each_here = json.loads(each)
    weights = []
    total_weight = 0.0
    for i in range(k):
        total_weight += each_here[i][1]
    for i in range(k):
        weights.append(k * each_here[i][1] / total_weight)
    for i in range(k):
        if each_here[i][0] in result_dict:
            result_dict[each_here[i][0]] += (count * weights[i])
        else:
            result_dict[each_here[i][0]] = (count * weights[i])

for each in result_dict:
    result_list.append((each, result_dict[each]))

result_list.sort(key=function, reverse=True)
print(result_list)

with open('bloc.txt', 'w') as f:
    for item in result_list:
        f.write("%s\n" % str(item))