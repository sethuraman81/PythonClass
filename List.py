'''

#List is mutable -- hence not hashable
#List mixed data types
#List can be indexed
#negative indexing
#
'''
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist = ["orange", "Mango", "Neuter", range, range, range(5)]
print(thislist)

mixed_list = [1, 'abc', True, 2.34, None]
print(mixed_list)

#negative indexing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#length of a list - gives number of items in a list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#looping through a list
for index,item in enumerate(thislist):
 print("item is : ", item, ", item's id is", id(item))
#write a while loop for the above
i=0
len(thislist)
while i<len(thislist):
    print(thislist[i])
    i+=1


#check if item exists in the list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


##append  -- what will be the output?
a = [1, 2, 3, 4, 5]
a.append(6)
a.append(7,)
a.append([80, 90]) #1, 2, 3, 4, 5,6,7,[80,90]
print(a)

a = [1, 2, 3, 4, 5, 5]
a.append(range(3))
print (a)

##what is the output?
a = [10, 2, 30, 40, 5, 5]
b = [10,20]
a.append(b)
print (a)

#append adds to the end of the list
#if to be added at specific position use
thislist = ["apple", "banana", "cherry"]
for item in enumerate(thislist):
 print(item)
print("++++++++++++")
thislist.insert(2, "orange")
print(thislist)

####Removing Items
#remove - removes first matching value
thislist = ["apple", "banana", "cherry","banana"]
thislist.remove('banana')
print(thislist)

#pop removes items from the end or by index and returns the value that is popped
a = [0, 1,99, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
print(a.pop(2))
print(a)

names = ['Alice', 'Craig', 'Diana', 'Diana', 'Eric', "Bob"]
print(names)
print(id(names))
print(type(names))
print(len(names))
print("+++++++++++++++++++")
for item in enumerate(names):
 print(item)
print("+++++++++++++++++++")
print (names.pop(4))
print (names)
print(len(names)) ###what will be the new length ?
print(id(names)) ##what will be the id of list after popping?

####del Keyword

a = list(range(10))
print(a) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del a[::2] #[1, 3, 5, 7, 9]
print(a) # what will be the output
del a[-1]
print(a) #[1, 3, 5, 7]
del a[:]
print(a)
del a ##what will happen in this command? --entire object of list

#can also be specified as
a = list(range(10))
print(a)
del(a)

# get Positional index of an item value from the list
#Syntax index(value, [startIndex],[stop])

a = [10, 20, 30, 40, 50, "AAA", 50,]
print(a.index(40))
print(a.index(50,1,-2))
#b=a.index(55) ##gives error if not found
#raises a ValueError exception and program flow will get interrupted
#to resolve that use a type safe check
if 55 in a:
 print(a.index(55))
else:
 print("That element 55 is not avaialable")



#clear
print("++"*20) #
print(a)
#a.clear() #removes all elements from the list equivalent to del a[:]
#print(a)

a = [10, 20, 30, 40, 50, 50, "AAA"]
print (a.reverse()) # reverse function returns None
#what is the alternative method of reversing a sequence?
print (a)

#count function identifies the number of occurences of a value
print(a.count(50))

#sort -- sort a list numerically or Lexicographically ?? - ascii number
#if custom sort is required write a function / lambda function and pass the parameter
lst = [10, 50, 20, 30, 40, 50, 100, 50,]
lst.sort()
print(lst.sort(reverse=True))
print (lst)
print("++"*20) #
###default sort won't work if there are mixed datatypes
lst = ['a', 'c', 's', 'a',]
lst.sort(reverse=True)#reverese sort can be achieved by specifying the parameter
print (lst)
lst = [('100','a',1,2,3), (500,'c',1,34,55,67), (900,'s',4,56,7), (999,'a',34,56)]

def fun(item):
    print(f"Item Received for sorting is {item}")
    if(len(item)>4):
        if(type(item[4])==int):
            return item[4]
        else:
            return int(item[4])
    else:
        return item[0]
lst.sort(key=fun,reverse=True)
print(lst)

def square(x):
    x *=x

a=5
square(a)
print(a)

a=[0,1,2,3,4]
print(a)
print(id(a))
b=a #shallow copy
b=a.copy() #deep copy
print(type(b))
print(id(b))
#constructor
c = list(a) #deep copy
print(id(c))
c[1]=99
print(c)
print(a)
d = a+b #List a.__add(listb)
print(d)

newlist = ['a','b','c']
#2,3,4,5,6,7,8,9,10
#2,4,6,8
newlist.extend(range(2,10,2)) #start,stop,step
print(newlist)

for i in range(10):
 print(i)
print("===========")

print(list(range(10)))
print("===========")
list1 = [10,20,30]
list1.extend(range(10))
print(list1)

a = [1, 2, 3, 4, 5, 5]
b = [10, 20, "A", "BBB"]
print (a + b) # WE USE + OPERATOR TO CONCANTENATE 2 LISTS /


silapthikaram = ["சிலப்பதிகாரம்", 21, "Sr.Data Analyst", "Single", "Ph.D", "Canara Bank",
"sb_54", False]
print(silapthikaram) #all of list
print(silapthikaram[:]) #entire list
print(silapthikaram[ 1:5 ]) #21, "Sr.Data Analyst", "Single", "Ph.D"
for index, item in enumerate(silapthikaram):
 print(index, item) #0,silapathikaram

 #5 ways of copying

 #shallow copy = assignment operator & .copy

 #deep copy - .deepcopy
 #list() --constructor -- deep copy
import copy
ss = copy.deepcopy(silapthikaram)
print(id(ss))
print(ss)
a=ss[:] #deep copy
print(id(a))


