import random
secrets = random.randint(1,10)
guess = int(input("1 se 10 tak number guess karo; "))
if guess == secrets:
    print("sahi jabab")

else:
    print("galat jabab")
    print(" sahi number tha:",secrets)


