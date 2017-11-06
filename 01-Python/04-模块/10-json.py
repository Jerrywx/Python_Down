
import json


# json 写入
# dic = {"name" : "wxiao", "age" : "22"}
#
# data = json.dumps(dic)
# print(data)
#
# f = open('json_txt', "w")
# f.write(data)
# f.close()


# json 读取
f = open("json_txt", "r")
data = f.read()
data = json.loads(data)
print(data)
print(data["name"])