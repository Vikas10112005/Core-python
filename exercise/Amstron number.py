number= 153
n = number
sum = 0
r = 0

while n > 0:
    r = n % 10
    sum = sum + r * r * r
    n = n // 10

if sum == number:
    print("this is amstrong", n)
else:
    print("not arms")