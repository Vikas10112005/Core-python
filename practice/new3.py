numbers=370
num=numbers
r=0
sum=0

while num > 0:
    r = num % 10
    sum = sum + r * r * r
    num = num//10

print(num)

if numbers ==sum:
    print("yes")

else:
    print("no")