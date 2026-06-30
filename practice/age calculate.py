import datetime
today = datetime.date.today()
my_date = datetime.date(year=2020,month=1,day=12)
age = today.year - my_date.year
print(age)
