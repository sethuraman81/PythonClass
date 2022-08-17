import copy
orignalList = [10, 20, 3,["Lin", "mel"]]
print("Original list",orignalList)
print("ID of the original list : ", id (orignalList))
for item in (orignalList):
    print(id(item))
print("===================")
duplicateList = copy.copy(orignalList)
print("ID of the duplicate list : ", id (duplicateList))
for item in (duplicateList):
    print(id(item))
print("===================")

duplicateList[2]="Test"
print(duplicateList)
print(orignalList)
