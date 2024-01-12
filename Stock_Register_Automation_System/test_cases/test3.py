import json
dic = {"A":1, "B":2}
print(dic)
file = open("FinalProducts.json", "w")
json.dump(dic, file, indent =2)