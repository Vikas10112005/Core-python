from abc import ABC, abstractmethod


# Base Class (Parent Class)
# ABC lagane se 'Animal' ek adhoori class ban gayi
class Animal(ABC):

    # Iska matlab: Har janwar ki apni ek 'make_sound' (aawaaz) honi chahiye!
    @abstractmethod
    def make_sound(self):
        pass


# Child Class (Kutta)
class Dog(Animal):
    def __init__(self, name):
        self.name = name

    # Animal class ke adhoore method ko yahan poora kiya
    def make_sound(self):
        return f"{self.name} bhonkh raha hai: Woof Woof!"


# --- Code kaise chalega ---

# 1. Normal Tareeka: Direct Dog class ka object banaya
d = Dog("Tommy")
print("Dog Sound:", d.make_sound())


# 2. Polymorphism: Reference type 'Animal' hai, par object 'Dog' ka hai
pet: Animal = Dog("Tommy")
print("Pet Sound (Animal reference se):", pet.make_sound())
# Isme Ho Kya Raha Hai? (1 Minute Me Samajhiye)
# Animal(ABC): Yeh Parent class hai. Isne rule bana diya ki "Jo bhi Animal banega, usko make_sound() method likhna hi padega."
#
# Dog: Isne Animal class ko follow kiya aur apna make_sound() define kiya (Woof Woof!).
#
# pet: Animal = Dog("Tommy"): Yeh dikhata hai ki hum variables me Parent (Animal) ka name likh kar bhi Child (Dog) ka kaam karwa sakte hain (Polymorphism).