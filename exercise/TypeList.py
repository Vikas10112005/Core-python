list = [10,20,30,40,50,60,70,80,]
list.append(90)               # add element
print(list)
print(list.count(10))         # count element
print(list.index(20))         # place of element
list.insert(2 , 25) # add new element
print(list)
list.remove(40)                # remove element
print(list)
list.reverse()                 # reverse list
print(list)
list.sort()                    # sort the list
print(list)
print(max(list))
print(min(list))
print(len(list))                # count element
print(sum(list))

list = (1,2,3,4,5,6,7,8,)
list1 = (9,10,11,12,13,14)
list2 = list + list1
print(list2)

list = [10,20,30,40,50,60,70,80]

high = 0

for i in list:
    if i > high:
        high = i
print("highest number=", high)
