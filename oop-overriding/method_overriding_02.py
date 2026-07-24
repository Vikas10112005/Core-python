# Base class (Parent class)
class Vehicle:
    def start(self):
        print('Vehicle Start Method')
        self.drive()  # Dynamic dispatch: Jis class ka object hoga, uski drive() call hogi

    def drive(self):
        print('Vehicle Drive Method')  # Default behavior (agar child override na kare)


# Child class 1: drive() ko override kar raha hai
class Car(Vehicle):
    def __init__(self, speed, gear):
        self.speed = speed
        self.gear = gear

    def drive(self):
        print(f'Car is driving at {self.speed} km/h in gear {self.gear}')


# Child class 2: drive() ko override kar raha hai
class Bike(Vehicle):
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print(f'Riding a {self.brand} bike!')


# Child class 3: Isne drive() ko override nahi kiya hai
class Truck(Vehicle):
    pass  # Kuch naya nahi banaya, toh parent ki drive() use karega


# --- Execution / Testing ---

# 1. Car ka object
c = Car(120, 5)
c.start()  # Output: Vehicle Start Method -> Car is driving at 120 km/h in gear 5

print('---')

# 2. Bike ka object
b = Bike('Yamaha')
b.start()  # Output: Vehicle Start Method -> Riding a Yamaha bike!

print('---')

# 3. Truck ka object
t = Truck()
t.start()  # Output: Vehicle Start Method -> Vehicle Drive Method (Fallback to parent)