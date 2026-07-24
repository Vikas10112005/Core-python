
class A:

    # Method 1: Jab koi argument pass nahi hoga
    def show(self):
        print("welcome")

    # Method 2: Jab sirf firstname pass hoga
    def show(self, firstname=""):
        print("welcome", firstname)

    # Method 3: Jab firstname aur lastname dono pass honge
    # Python me actual method overloading nahi hoti.
    # Isliye last wala method hi previous methods ko replace kar deta hai.
    # Default arguments ki help se overloading jaisa behaviour create kiya gaya hai.
    def show(self, firstname="", lastname=""):
        print("welcome", firstname, lastname)


# Object create kiya
obj = A()

# Method ko bina argument ke call kiya
obj.show()

# Sirf firstname pass kiya
obj.show("vikas")

# Firstname aur lastname dono pass kiye
obj.show("vikas", "verma")