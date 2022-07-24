import datetime
aDate = not None
aDate = aDate or datetime.date.today()
print(aDate)
print(type(aDate))
print(id(aDate))