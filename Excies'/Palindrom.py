numbers = 121
num=numbers
rev=0

while num > 0:
    r = num % 10
    rev = rev * 10 + r
    num = num // 10

print(rev)

if numbers == rev:
    print("This is Palindrom No..")
else:
    print("This is Not Palindrom No..  ")