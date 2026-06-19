numbers = 123
num = numbers
r = 0
a = 0

while num > 0:
    r = num % 10
    a = a * 10 + r
    num = num // 10

print (num)


