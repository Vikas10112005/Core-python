import pickle
from write_object import Employee

with open("C:/Users/hp/PycharmProjects/CorePython/file/write_binary.py", 'rb') as file:
    obj = pickle.load(file)
    print("Printing Employee information after unpickling")

obj.display()