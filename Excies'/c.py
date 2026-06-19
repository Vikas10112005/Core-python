numbers = 456
num=numbers
r=0
sum=0

while sum > 0:
    r = num % 10
    sum = sum*10+r
    num=num//10

print(num)

numbers = 455
num=numbers
r=0
sum=0

while sum > 0:
    r = num % 10
    sum = sum*10+r
    num=num//10

print(num)

numbers = 12
num  = numbers
r=0
sum=0

while sum > 0:
    r = num % 10
    sum = sum + r * r *r
    num=num//10

print(sum)

if numbers == sum:
     print(" THis is  Amstrong No...")

else:
    print(" Thsi is not Amstrong No..")
