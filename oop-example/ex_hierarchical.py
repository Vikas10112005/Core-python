
# parent class
class animal:
    def eat(self):
        print("animal is eating")

# child class (inherit parent class)
class dog(animal):
    def bark(self):
        print("dog is barking")

#second child class (inherit parent class)
class cat(animal):
    def meow(self):
        print("cat is meowing ")

#third child class (innherit parent class)
class snake(animal):
    def hiss(self):
        print("snake sound hissed")

d = dog()
d.eat()
d.bark()
print("_______")
c=cat()
c.eat()
c.meow()
print("_______")
s=snake()
s.eat()
s.hiss()
