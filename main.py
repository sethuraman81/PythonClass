def mult(*a):
 for i in a:
  c=c*i

#Kw pair
#lambda
#Classes - Objects
#selenium

def add(v1, *, v2,v3=0):
    print('arg1: ', v2)
    print('arg2: ', v3)

add(35,v2=45,v3=56)

print("Calling add function " ,add(3,v2=4))
