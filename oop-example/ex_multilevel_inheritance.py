
# parent class
class animal:
    def eat(self):
        print("animal is eating")

# child class (inherit parent class)
class dog(animal):
    def bark(self):
        print("dog is barking")

class puppy(dog):
    def sleep(self):
        print("puppy is sleeping")
#object
obj=puppy()

obj.eat() #parent class method
obj.bark() #child class method
obj.sleep() #grand child class