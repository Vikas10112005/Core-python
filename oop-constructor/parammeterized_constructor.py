
class student:
    def __init__(self,name,age,dob):
        self.name = name
        self.age = age
        self.dob = dob

    def getname(self):
        return self.name
    def getage(self):
        return self.age
    def getdob(self):
        return self.dob

s = student("vikas",20,"10,11,2005")
print("name=",s.getname())
print("age=",s.getage())
print("dob=",s.getdob())