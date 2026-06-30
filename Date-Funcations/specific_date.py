import datetime

today = datetime.date.today()
my_date = datetime.date(2005, 11, 10)

age = today.year - my_date.year

print("this is my age",age)
# print("My birth  date ", my_date)

today = datetime.date.today()
my_date = datetime.date(year=1998,month=10,day=2)
age = today.year - my_date.year

print("it's my age",age)
