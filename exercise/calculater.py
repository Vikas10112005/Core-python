# calculater
num1 = float (input("phela number lekho:  "))
num2 = float (input("dusra number lekho:  "))

operator = input("operation choose karo (+,-,*,/,**,): ")

if operator == "+":
    print("answer=", num1 + num2)

elif operator == "-":
    print("answer=", num1 - num2)

elif operator == "*":
    print("answer=", num1 * num2)

elif operator == "/":
    print("answer=", num1 / num2)

else:
    print("galat operator")