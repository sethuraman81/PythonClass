
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