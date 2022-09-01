#no duplicates
#set()
#{} --will take dictionary
#intersection symbol --&
#union symbol -- |
#difference --  symbol -
#symmetric difference -- ^ --inverse of intersection ---excludes common items
#Set is Mutable -- frozen set not mutable
#set elements must be immutable
a= {1,2,3,4,5,6,7}
b={1,2,3}
c=1
print(type(a))
print(type(c))
print(b<=a)
print(a >= b  ) #polymorphism

a = {'A', 'B', 'C'}
b= {10,20,30,30}
a.update(b)
print(a)



