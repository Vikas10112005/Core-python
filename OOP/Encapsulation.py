from _datetime import datetime

class Person:
    AVG_AGE = 18

    def __init__(self):
        print(" Cons is calliing  ther person class")
        self.__name = None
        self.__dob = None
        self.__address = None


    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_dob(self):
        return self.__dob

    def set_dob(self, dob):
        self.__dob = dob

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_age(self):
        if self.__dob is None:
            return None

        now = datetime.now()
        age = now.year - self.__dob.year
        return age


p = Person()
p.set_name("vikas")
p.set_address("bhopal")
p.set_dob(datetime(2005, 11, 10))

print("Name:", p.get_name())
print("Age:", p.get_age())
print(p.get_dob())
print(Person.AVG_AGE)

p1 = Person()
p1.set_name("sandy")
p1.set_address("Indore")
p1.set_dob(datetime(2000, 11, 11))

print("Name:", p1.get_name())
print("Age:", p1.get_age())
print(p1.get_dob())
