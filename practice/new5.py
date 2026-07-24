numbers=4774
num=numbers
r=0
sum=0

while num > 0:
    r = num % 10
    sum = sum*10+r
    num = num // 10

print(sum)

if numbers ==sum:
    print("yes")

else:
    print("no")