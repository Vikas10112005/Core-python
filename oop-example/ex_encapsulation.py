class student:

    def __init__(self):
        print("student class")
        self.__name = None
        self.__standerd = 0
        self.__rollno = 0

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_standerd(self):
        return self.__standerd

    def set_standerd(self,standerd):
        self.__standerd = standerd

    def get_rollno(self):
        return self.__rollno

    def set_rollno(self,rollno):
        self.__rollno = rollno

s = student()
s.set_name("vikas")
s.set_standerd(10)
s.set_rollno(1001)

print("name=",s.get_name())
print("standerd=",s.get_standerd())
print("rollno=",s.get_rollno())

