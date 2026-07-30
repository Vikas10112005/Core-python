try:
# yaha wo code likhte h jinme error aa skti h
 a = 10
 b = 0
 c = a/b
 print("division:",c)

except ZeroDivisionError as e:
    # error yaha par handle ho jayega
    print('exception:',e)

else:
    #ye jabbhi chalega jb try block me koi error na ho
    print("else block run")

finally:
    #ye block hamesh chalega error ayee ya na ayee
    print("program finished")

