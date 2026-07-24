class animal:
    def sound(self):
         print("animal make sound")

class dog(animal):
    def sound(self):
        print("dog barks")
        super().sound() # parent class ki method ko print karwa liya.

d = dog()
d.sound()


