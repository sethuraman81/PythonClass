"""


class Student:
 def __init__(self,name,school):
  self.name=name
  self.school = school
  self.marks = []

 def average(self):
  return sum(self.marks)/len(self.marks)

 def __eq__(self,tempst):
  print("Self Average = ",self.average())
  print("Param Average = ", tempst.average())
  return self.average() == tempst.average()

class WorkingStudent(Student):
 def __init__(self,name,school,salary):
  super().__init__(name,school)
  self.salary = salary

stu1 = Student('Arun','National')
stu1.marks.append(50)
stu1.marks.append(60)
stu1.marks.append(70)

stu2 = Student('Sasi','BAM')
stu2.marks.append(60)
stu2.marks.append(70)
stu2.marks.append(80)

stu3 = WorkingStudent('Manoj','Hindustan',3000)
stu3.marks.append(60)
stu3.marks.append(70)
stu3.marks.append(80)

print( stu2.__eq__(stu1))
print("++++")


a,*b,c=(1,2,3,4,5,6,7,78,88,97,34)
print(*b)
first, *more, last = (1, 2, 3, 4, 5, 6)
print (first)
print(more)
print(*more)
print (last)

a=(1,2,3,4,5,6)
b=(1,2,3,4,5,6)
print(a.__eq__(b))

st = {'hello'}
print(type(st))
a= (frozenset(), 1)
print(hash(a))



tuple1 = (1, 2, 3, )

print (hash(tuple1))
tuple2 = (1, 2, 3, )
print (hash(tuple2))
print(tuple1.__eq__(tuple2))
print("----***")
print(id(tuple1))
print(id(tuple2))




colors = "red", "green", "blue"
ab=tuple(reversed(colors))
print(ab)

one_member_tuple = 'Only member'
print(type(one_member_tuple))

first,last, *more = (1,2)
print(first)
#print(last)
print(*more)
a,b,c=1,2,3
print(a,b,c)

t1= list(range(4))
t2= list(range(10))
a = [t1,t2]
print(a)
b=a[::2]
print(b)
#list[ start : stop: step]

from abc import ABC, abstractmethod

class Garages:
 newlist=[]
 def __init__(self):
  self.cars=[] #constructor
  self.cars1=[]
  self.tup=(1,2,3)

 def __hash__(self):
  return hash(self.tup)
 def __len__(self):
  return len(self.cars)
 def __getitem__(self, item):
  return self.cars1[item]
 def __repr__(self):
  return f'<Garage {self.cars}>'


#Gurukulam --abstract
#electrical
#Welding


Garages.newlist.append('AllCars')
Garages.newlist.append('Fiat')
Garages.newlist.append('Maruti')

ford=Garages() #constructor --list create--cars
mercedes=Garages() #constructor --list create--cars

ford.cars.append('Fiesta')
ford.cars.append('Focus')
ford.cars1.append('F12')
ford.cars1.append('Foc12')


mercedes.cars.append('A class')
mercedes.cars.append('S class')


for i in ford:
 print(i)
 print(ford.newlist)



for i in mercedes:
 print(i)
 print(ford.newlist)

 for i in Garages.newlist:
  print(i)




def fun(item):
    if item!='python':
        return item

lst2=['python','list','append','python']

for i in range(0,len(lst2)):
    lst2[i] = ''

print(lst2)
print(len(lst2))


ab = list(filter(fun,lst2))
print(ab)
print(len(ab))

#pop -- last and by index
#lambda functions -- one line conditions
#simple for loop
#clear
#del
#remove
#filter



Binary to decimal conversion Classwork
def convertnumbertoBin(a):

    print(a)
    bstr=bin(a)
    print(bstr)
    bstr = bstr[2:]
    bstr= bstr.zfill(8)
    print(bstr)
    bstr = bstr[::-1]
    print(bstr)
    ab= int(bstr,2)
    print(ab)

convertnumbertoBin(56)

palindrome = int(input("Enter the Maximum Value:"))
print("palindrome numbers 1 and %d are:"% palindrome)
for num in range(1, palindrome + 1):
    temp = num
    reverse = 0
    while(temp > 0): #1000
        reminder = temp % 10 #
        reverse=(reverse * 10)+reminder #99
        temp = temp//10 #0
    if(num == reverse):
        print("%d"%num,end=' ')

"""

"""
def funct (*a,sep="$$$"):
    for idx,i in enumerate(a):
        print (i, end='')
        if(idx+1 < len(a)):
            print(sep,end='')

funct(20,30,40,sep="---")

"""


"""

def foo(m): #5
    if m ==0:
        return(0)
    else:
        return(m+foo(m-1)) #15
print(foo(5))


0-0
1 -1
2- 2+1+0 =3
3 - 3+3 =6
4 - 4+6=10
5- 5+10 =15
6- 6+15 =21
7-7+21=28
8-8+28 = 36
n*(n+1)/2
"""



"""


def add(*a,str):
    print (f"value a = {a}\n value of str = {str}")
    #print(sum(a))
    #

add(20,20,30,40,"example",str="Keyword argument")

def func(*,a,b,c):
    print (a,b,c)
    print("all keyword parameters")

func(a=20,b=30,c=50)



"""



"""

a = 3
if a in (3, 4, 6):
    print("Yes")
else:
    print("No")

a="Hello"
b=a
print (id(a))
print (id(b))
if a is b:
    print("Same ID's")

a = 3
if a == 3 or a == 4 or a == 6:
    print("Yes")
else:
    print("No")


print(1 or 2) #1
print(0 or 2) #2
print(None or 5) #5
print(False or 6 ) #6
print(True or False) #True
print(False or True) #True

print([] or True) #True
print([] or 0 or {}) #{}
print([] or "ABC" or {22})

print(None or None  )

print(0 or {} or [])

print(0 or (10-10) or "BB")

def testfun():
    print("Hello There")
    #return None

a = 3 and testfun() and 6
print(a)


a = " " and "Linda" and " " and None and []
print(a)

a= 5 and 1 and 2
print(a)


if True:
    print("it prints")
else:
    print("it does not print")

if False:
    print("it prints")
else:
    print("it DOES print")
"""




def func1():
    a = "abc"
    print(id(a))
    b = a
    print(type(a))
    print(type(b))
    print(id(b))

    c = "abcd"
    c = c[0:3]
    print(type(c))
    print(id(c))
    print(c)

    if (a == b):
        print("content is true")

    if (a is not c):
        print("Same memory location")

#############
def foo():
    return ""
print(id(foo))
if foo:
    print("print somthing")
else:
     print("No value returned from a function")
################################


print(1 and 2 and None and 4)

print(1 and 2 and -5 and 4 and 5 and { } )

print(1 & 2 & 3 & 4)

print(" " and "Py" and "")
a="abc"
print(repr(a))# “”
print(f"value of  {repr(a)}----")

abc=55
print(f"value of variable {abc} is --55 \n\n\n---")
print("value of variable  is " ,abc)
print(r"\n\n\t")



"""
0001
0010
0011
0100
0000---answer
"""

################

print ( 1 and 2 and 3 and 4 and 5 )

print( 0 or 0 or 0 or 0 or [] or None)

print([] or "ABC" or {22})#

print(0 or (10-10) or "BB")

print( [] or 0 or {})

print("Sir" and {} and 56)

print(True + True)