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