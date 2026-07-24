from _datetime import datetime

class Person:
    avg_age=20

    def __init__(self):
        print("that person class")
        self.__name = None
        self.__dob = None
        self.__address = None

    def get_name(self):
        return self.__name

    def  __set_name__(self, name):
        self.__name = name

    def get_dob(self):
        return self.__dob

    def __set_dob__(self):
       self.__dob

    def get_address__(self,name):
        return self.__address

    def __set_address__(self):
        return self.__address

    def get_age(self):
        if self.__dob is None:
            return None

        now = datetime.now()
        age = now.year - self.__dob.year
        return age


p = Person()
p.__set_name__("vikas")
p.__set_address__("bhopal")
p.__set_dob__(datetime(2005,11,10))


print("Name:", p.get_name())
print("Age:", p.get_age())
print(p.get_dob())
print(Person.AVG_AGE)

