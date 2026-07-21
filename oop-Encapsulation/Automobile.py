class Automobile:

    def __init__(self):
        self.__color = None
        self.__speed = 0
        self.__make = None

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

car = Automobile()
car.set_color("black")
car.set_make("bmw")
car.set_speed("550")

print("car colour=",car.get_color())
print("car maker=",car.get_make())
print("car speed=",car.get_speed())