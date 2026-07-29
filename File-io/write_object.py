import pickle



class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):
        print(self.id, "\t", self.name, "\t", self.salary)


with open("C:/Users/hp/PycharmProjects/CorePython/file/write_binary.py", 'wb') as file:
    emp = Employee(1, 'vikas', 12121212)
    pickle.dump(emp, file)