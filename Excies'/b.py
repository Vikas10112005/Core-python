numbers = 371
num = numbers
r=0
sum=0
while num > 0:
    r = num % 10
    sum = sum*10+r
    num=num//10

print(sum)

numbers = 153
num = numbers
r = 0
sum = 0

while num > 0:
    r = num % 10
    sum = sum + r * r * r
    num = num // 10

print(sum)
