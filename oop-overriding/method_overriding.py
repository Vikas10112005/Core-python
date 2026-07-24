class A:
    # parent class method

    def disp(self):
        print("this is parent class method")

   # child class method overriding
   # child class ne parent class ke same method ko override kiya h
   # redefine parent class method by child class

class B(A):
    def disp(self):
        print("this is child class method")

   # parent class ke method ko call karne ke liye super() keyword ka use kiya.
        super().disp()

# child class ka object creat kiya.
obj=B()

#child class ki method call ki.
obj.disp()
