from pyvotecore.stv import STV
import json

f = open("count.json", "r")
input_json = json.load(f)
f.close()

input_list = []

for each in input_json:
    dict_here = {"count": input_json[each], "ballot": json.loads(each)}
    input_list.append(dict_here)

output = STV(input_list, required_winners=15).as_dict()
print(output)


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


with open('stv.txt', 'w') as f:
    f.write(str(output))

with open('stv.json', 'w') as f:
    json.dump(output, f, cls=SetEncoder)
