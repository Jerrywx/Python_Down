import json

d = {'a': 'aaa', 'b': ['b1', 'b2', 'b3'], 'c': 100}
json_str = json.dumps(d)
print(json_str)