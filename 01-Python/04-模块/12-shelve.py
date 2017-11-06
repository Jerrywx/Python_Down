
import shelve

f = shelve.open('shelve_txt')

# f["test"] = {"name" : "wxiao",
#              "age" : "26"}
# f.close()

# data = f.get("test")

data = f["test"]
print(data)