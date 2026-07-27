
# parent class
class animal:
    def eat(self):
        print("animal is eating")

# child class (inherit parent class)
class dog(animal):
    def bark(self):
        print("dog is barking")

#object
obj=dog()

obj.eat() #parent class method
obj.bark() #child class method