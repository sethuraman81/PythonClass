import datetime
class Person(object):
 def __init__(self, name, birthday, height):
  self.name = name
  self.birthday = birthday
  self.height = height
 def __repr__(self):
  return self.name

l = [Person("John Cena", datetime.date(1992, 9, 12), 175),
 Person("Chuck Norris", datetime.date(1990, 8, 28), 180),
 Person("Jon Skeet", datetime.date(1991, 7, 6), 185)]
l.sort(key=lambda item: item.name)
# l: [Chuck Norris, John Cena, Jon Skeet]
l.sort(key=lambda item: item.birthday)
# l: [Chuck Norris, Jon Skeet, John Cena]
l.sort(key=lambda item: item.height)
# l: [John Cena, Chuck Norris, Jon Skeet]


xs = ['a', 'b', 'c', 'd', 'b', 'b', 'b', 'b']
xs = [x for x in xs if x != 'b']
print(xs)
