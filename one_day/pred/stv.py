from pyvotecore.stv import STV
import json

f = open("count.json","r")
input_json = json.load(f)
f.close()

input_list = []

for each in input_json:
	dict_here={}
	dict_here["count"] = input_json[each]
	dict_here["ballot"] = json.loads(each)
	input_list.append(dict_here)

output = STV(input_list, required_winners=3).as_dict()
print(output)