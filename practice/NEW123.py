numbers = 153
num  = numbers
r=0
sum=0

while num > 0:
    r = num % 10
    sum = sum + r**3
    num=num//10

print(num)

if numbers == sum:
    print("this is amstrong")

else:
    print("this is not amstrong")