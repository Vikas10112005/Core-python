
class Person:
    # constructor
    def __init__(self):
        # instance variable
        self.name = "No name"

    # Method
    def display(self, name):
        print("Hello", name)


obj = Person()
obj.display("Ram")
obj.display("Shyam")