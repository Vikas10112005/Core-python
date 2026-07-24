class student:
    # constructor
    def __init__(self,name,age):
    #object ke andar data save karna
     self.name=name
     self.age=age

    #method
    def show(self):
        #object ka data print karna
        print("name:",self.name)
        print("age",self.age)

#object bana rahe h
s1 = student("vikas",20)
#method call
s1.show()

