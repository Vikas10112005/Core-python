numbers = 313
n=numbers
r=0
s=0

while n > 0:
    r = n % 10
    s = s + r * r * r
    n = n // 10

print(s)

if numbers == s:
    print("yes")

else:
    print("no")

