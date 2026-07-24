# Base Class (Parent)
class User:
    def execute(self):
        # Pehle validate karega ki user active/allowed hai ya nahi
        if self.validate():
            self.show_profile()
        else:
            print("Validation Failed: Access Denied!")

    def validate(self):
        # Default rule: Unknown users ke liye Validation False
        return False

    def show_profile(self):
        print("Default User Profile")


# Child Class 1: Admin User
class Admin(User):
    def __init__(self, username, is_active):
        self.username = username
        self.is_active = is_active

    # Admin ka validation: Active hona chahiye
    def validate(self):
        if self.is_active == True:
            return True
        else:
            return False

    # Admin ka apna profile display (Method Overriding)
    def show_profile(self):
        print(f"Welcome Admin: {self.username} (Full Access Granted)")


# Child Class 2: Student User
class Student(User):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Student ka validation: Age 18 ya usse zyada honi chahiye
    def validate(self):
        if self.age >= 18:
            return True
        else:
            return False

    # Student ka apna profile display (Method Overriding)
    def show_profile(self):
        print(f"Student Profile: {self.name}, Age: {self.age}")


# Child Class 3: Guest User (Isne kuch override nahi kiya)
class Guest(User):
    pass  # Kuch naya nahi banaya


# --- Execution / Testing ---

print("\n--- Admin Login ---")
a = Admin("Rahul_Admin", is_active=True)
a.execute()

print("\n--- Student Login ---")
s = Student("Aman", age=20)
s.execute()

print("\n--- Invalid Student (Underage) ---")
s_invalid = Student("Rohan", age=15)
s_invalid.execute()

print("\n--- Guest Login ---")
g = Guest()
g.execute()