class Person:

    def __init__(self):
        print("person class")
        self.__name = None
        self.__dob = None
        self.__address = None

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_dob(self):
        return self.__dob

    def set_dob(self,dob):
        self.__dob = dob

    def get_address(self):
        return self.__address

    def set_address(self,address):
        self.__address = address

p = Person()
p.set_name("vikas")
p.set_dob("2005,11,10")
p.set_address("bhopal")

print("name:",p.get_name())
print("dob:",p.get_dob())
print("address:",p.get_address())

