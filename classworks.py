



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