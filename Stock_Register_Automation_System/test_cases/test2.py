import json
dic = {"A" : {"a":1, "b":2}, "B" : {"c":3, "d":4}}
print(dic)
file = open("Qualities.json", "w")
json.dump(dic, file, indent =2)