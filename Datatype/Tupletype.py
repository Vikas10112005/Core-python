tuple = (1,2,3,4,5,6,7,8,)
print(type(tuple))
print(max(tuple))
print(min(tuple))
print(len(tuple))
print(sum(tuple))
print(tuple[0])
print(tuple[1])
print(tuple.count(4))
print(tuple.index(6))
print(5 in tuple)
print(tuple[1:5])
print(tuple[-1])

tuple = (1,2,3,4,5,6,7,8,)
tuple1 = (9,10,11,12,13,14)
tuple2 = tuple + tuple1
print(tuple2)

tuple = (1,2,3,4,5,6,7,8)

high = 0

for i in tuple:
    if i > high:
        high = i
print("highest number=", high)