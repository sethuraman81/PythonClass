a = {1,2,3,4,5,6}
b= {1,7}
print(a.isdisjoint(b))


a={1,2,3,4,5,6,7,'A','B','C',10,20,30}
b={3,4,5,6,20,30}
print(a)
a.pop()# random --
a.discard(56)

if 56 in a:
    a.remove(56)


#result after symmetric - 1,2,7
s1=set(a)
s2= set(b)
l1= list(s1.symmetric_difference(s2))
print(l1)

a= {'A','B','C',10,30,45}
a.pop()
a.discard(45)
if 65 in a:
    a.remove(65)
else:
    print("no such item 65")

print(a)


#a | b #union
# a & b #intersect
# a- b #difference
#symmetric difference
#no common values - disjoint - True



#union & update
#intersect - common