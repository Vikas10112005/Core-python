import  datetime
from time import strftime

d = datetime.datetime.now()
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)
print(d.microsecond)
print(d)
print(d.strftime("%d-%m-%y"))
print(d.strftime("%A, %B %d, %Y"))
print(d.min)
print(d.max)



# import  datetime
# today = datetime.date.today()
#
# print("Day", today.day)
# print("Month",today.month)
# print("Year",today.year)





import  datetime

today =datetime.date.today()
print("Current date:", today)

formated = today.strftime("%d-%m-%y")
# #
# #
print("Formatted date:", formated)