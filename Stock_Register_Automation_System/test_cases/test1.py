import json
dic = {"a":1, "b":2}
print(dic)
file = open("RawMaterials.json", "w")
json.dump(dic, file, indent =2)