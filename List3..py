"""
reference link -- python deep copy memory optimization
 https://towardsdatascience.com/assignment-shallow-or-deep-a-story-about-pythons-memory-management-b8fad87bfa6c
"""
import copy
import ctypes
orignalList = [10, 20, 3,["Lin", "mel"],(1,2,3),False]
duplicateList = copy.deepcopy(orignalList)

for index,item1 in enumerate(duplicateList):
 print(f"{item1}--- {index}={id(orignalList[index])}--- {id(duplicateList[index])}")

duplicateList[3]=31
for index,item1 in enumerate(duplicateList):
 print(f"{item1}--- {index}={id(orignalList[index])}--- {id(duplicateList[index])}")

print("===================")
x = id(orignalList[4])
print(f'ID OF {orignalList[4]}', f"{x}")
print("===================")
y = id(duplicateList[4])
print(f'ID OF {duplicateList[4]} == {y} ')
# a = ctypes.cast()
print("===================")
'''
access values from id
# get the value through memory address
a = ctypes.cast(x, ctypes.py_object).value
'''
a = ctypes.cast(x, ctypes.py_object).value
print(a) # it gives the content(Values or values) of the memory address

