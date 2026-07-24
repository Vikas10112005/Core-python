def welcome():
  print("welcome to the function")
welcome()

#greet
def greet(name):
    print("hello",name)
greet("rahul")
greet("priya")

#positional

def student(name,city):
    print(name,"lives in", city)

student("abhay", "indore")
student("payal", "mumbai")
#keyword argument
def movie(name,rating):
    print(name,"rating is",rating)
movie(rating=9,name="pushpa")

#default argument
def student(name,city="indore"):
    print(name, "lives in",city)
student("rahul","mumbai")
student("priya")

#args
def total_marks(*marks):
    print(marks)
total_marks(80,70,90,60)

#** kwargs

def student_info(**data):
    print(data)
student_info(name="rahul",city="indore")

#return statement
def add(a,b):
    return a+b
result = add(10,20)
print(result)

#multiple return value
def student():
    return "rahul",21,"indore"
name,age,city = student()
print(name)
print(age)
print(city)

#local variable
def demo():
    x = 10
    print(x)
demo()

#globle variable
college = "rays edtech"
def show():
    print(college)
def display():
    print(college)

show()
display()

#lambda functions
#nomal functions
def square(x):
    return x * x
print(square(5))
#lambda function
square = lambda x : x * x
print(square(5))

#recursive function
def factorial(n):
    if n== 1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

#higher order function

#map()

marks = [10,20,30]
result = list(map(lambda x:x*2,marks))
print(result)

#filter()
numbers = [1,2,3,4,5,6]
result = list(filter(lambda x:x%2==0,numbers))
print(result)

#reduce()
from functools import reduce
numbers=[1,2,3,4,5]
result = reduce(lambda a,b:a+b,numbers)
print(result)