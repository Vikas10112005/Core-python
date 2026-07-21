class Student:
    def getStudent(self):
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.gender = input("Gender: ")


class Test(Student):
    def getMarks(self):
        self.studentClass = input("Class: ")
        print("Enter the marks of the respective subjects")
        self.literature = int(input("Literature: "))
        self.math = int(input("Math: "))
        self.biology = int(input("Biology: "))
        self.physics = int(input("Physics: "))


class Marks(Test):
    def display(self):
        print("\n\nName:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Class:", self.studentClass)
        print("Literature:", self.literature)
        print("Math:", self.math)
        print("Biology:", self.biology)
        print("Physics:", self.physics)
        total_marks = self.literature + self.math + self.biology + self.physics
        if total_marks > 100:
            print("Passed")
        else:
            print("Failed")
        print("Total Marks:", total_marks)


m = Marks()

m.getStudent()

m.getMarks()

m.display()