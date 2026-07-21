# Parent Class
class Car:

    def __init__(self):
        # Default values set ki hain
        self.colour = "Black"
        self.make = "Tata Motors"
        self.speed = 180  # km/h

    def display_car_details(self):
        print(f"Car Make  : {self.make}")
        print(f"Car Colour: {self.colour}")
        print(f"Top Speed : {self.speed} km/h")


# Child Class (Inherits Car)
class CarPrice(Car):

    def __init__(self):
        super().__init__()  # Parent class ke constructor ko call kar rha hai
        self.main_price = 1000000  # Ex-showroom price
        self.onroad_price = 1150000  # On-road price

    def display_price_details(self):
        self.display_car_details()  # Parent class ka method call
        print(f"Main Price  : ₹{self.main_price}")
        print(f"On-Road Price: ₹{self.onroad_price}")


# Grandchild Class (Inherits CarPrice) - Multilevel Inheritance
class CarDelivery(CarPrice):

    def __init__(self):
        super().__init__()  # CarPrice class ke constructor ko call kar rha hai
        self.delivery_date = "15-August-2026"
        self.waiting_days = 45

    def display_all_details(self):
        print("=== CAR FULL DETAILS ===")
        self.display_price_details()  # CarPrice ka method call
        print(f"Delivery Date: {self.delivery_date}")
        print(f"Waiting Period: {self.waiting_days} Days")


# --- Object Creation & Testing ---
# Grandchild class ka object banayege jisme sabhi properties aayengi
my_car = CarDelivery()

# Sabhi details print karte hain
my_car.display_all_details()