import json
import datetime

def assertionValue(x, t=""):
    s = t + " gone negative. DISCRPENCY IN DATA"
    assert x>=0, s
    return


# making a copy of Raw Materials Qty dictionary
RawMaterialFile = open("RawMaterials.json", "r")
RawMatDict = json.load(RawMaterialFile)
RawMaterialFile.close()


# making a copy of Final Products Qty dictionary
FinalProductFile = open("FinalProducts.json", "r")
FinProdDict = json.load(FinalProductFile)
FinalProductFile.close()


# making a copy of Quality dictionary
QualityFile = open("Qualities.json", "r")
QualityDict = json.load(QualityFile)
QualityFile.close()


print (RawMatDict, FinProdDict, QualityDict)



# Preparation of the File string 
dt = datetime.datetime.now()
formatted_date = dt.strftime("%B %d, %Y - %I:%M %p")
FileString = formatted_date + '\n'


# Q1
FileString += "------RAW MATERIALS RECEIVED ON THIS DAY------\n"
# print("what raw material did you recieved today and in what quantity :")
print("----------WHAT RAW MATERIALS DID YOU RECIEVED TODAY AND IN WHAT QUANTITY----------")
for i in RawMatDict:
    ques = i + " -> "
    x = int(input(ques))
    # error check
    assertionValue(x)
    FileString += (i + " -> " + str(x) + " units\n")
    
    RawMatDict[i] += x
    
# Q2
FileString += "\n------FINAL PRODUCTS MANUFACTURED ON THIS DAY------\n"
# print("What final product did you produced today and in what quantity :")
print("----------WHAT FINAL PRODUCTS DID YOU PRODUCED TODAY AND IN WHAT QUANTITY----------")
for i in FinProdDict:
    ques = i + " -> "
    x = int(input(ques))
    # error check
    assertionValue(x)
    FileString += (i + " -> " + str(x) + " units\n")
    
    # updating final product quantity
    FinProdDict[i] += x
    
    
    # updating raw material quanity usedin making final product
    QlyDictOfi = QualityDict[i]
    for j in QlyDictOfi.keys():
        RawMatDict[j] -= x * QlyDictOfi[j]
        assertionValue(RawMatDict[j],j)
        # error check
        
#Q3
FileString += "\n------FINAL PRODUCTS DISPATCHED ON THIS DAY------\n"
# print("What Final Product did you dispatched and in what quatity : ")
print("----------WHAT FINAL PRODUCTS DID YOU DISPATCHED TODAY AND IN WHAT QUANTITY----------")
for i in FinProdDict:
    ques = i + " -> "
    x = int(input(ques))
    # error check
    assertionValue(x)
    FileString += (i + " -> " + str(x) + " units\n")
    
    FinProdDict[i] -= x
    assertionValue(FinProdDict[i], i)

# print (RawMatDict, FinProdDict)


# Raw Material Dictionary Data in Final String
FileString += "\n------NET RAW MATERIALS BALANCE------\n"

for x,y in RawMatDict.items():
    FileString += x + " -> " + str(y) + "\n"
    
    
# Final Product Dictionary data in Final String
FileString += "\n------NET FINAL MATERIALS BALANCE------\n"

for x,y in FinProdDict.items():
    FileString += x + " -> " + str(y) + "\n"


# Marking a finishing line for Clarity

FileString += "\n________________________________________________________________________________\n\n"


# Dumping FileSting  in Entry file
MainFile = open("EntryFile.txt", "a")
MainFile.write(FileString)
MainFile.close()







#Dumping dictionary in raw material file
RawMaterialFile = open("RawMaterials.json", "w")
json.dump(RawMatDict, RawMaterialFile, indent =2)
RawMaterialFile.close()


# Dumping dictionary in final product file
FinalProductFile = open("FinalProducts.json", "w")
json.dump(FinProdDict, FinalProductFile, indent =2)
FinalProductFile.close()
    
    
    







