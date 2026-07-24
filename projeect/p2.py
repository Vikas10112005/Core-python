# score = int(input("enter score:"))
# if score >= 180:
#     print("excellent batting")
# elif score >= 100:
#     print("average batting")
# else:
#     print("weak batting")


score = int(input("enter score:"))
over = int(input("enter over"))
run_rate = score / over
print("run rate=",run_rate)
if score >= 180:
    print("excellent batting")
elif score >= 100:
    print("average batting")
else:
    print("weak batting")

