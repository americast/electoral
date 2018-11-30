import json

f = open("count.json","r")
input_json = json.load(f)
f.close()

def function(elem):
	return elem[1]

result_dict ={}
result_list = []
for each in input_json:
	count = input_json[each]
	each_here = json.loads(each)
	list_here = [i for i in range(len(each_here)-1,-1,-1)]
	for i in range(len(each_here)):
		if each_here[i] in result_dict:
			result_dict[each_here[i]]+=list_here[i]*count
		else:
			result_dict[each_here[i]]=list_here[i]*count


for each in result_dict:
	result_list.append((each,result_dict[each]))

result_list.sort(key=function,reverse=True)
print(result_list)