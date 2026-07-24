class Person:
    def __init__(self, name, age): # constructor run when object call
        print("Hello init method.... cons is calling ")
        self.name = name # yaha kuch value de jayegi to usko attribute bolenge
        self.age = age

    def __del__(self): # object ya attribute ko delete karta h # destructor
        classname = self.__class__.__name__ # local variable
        print("Destroying ", classname)

    def __str__(self):  #object ko print karta h
        print(" Hello Str Method....")
        return "Person: name = %s, age = %s" % (self.name, self.age)


person = Person("abc", 30) #object1
p=Person("xyz", 25) #object2
print(person) #  str method ko call
print(p) # str  method ko call
