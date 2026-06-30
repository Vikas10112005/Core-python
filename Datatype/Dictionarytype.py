d= {'a':1 ,'b':2,'c':3,'d':4,'e':5}
print(d.get('b'))   # get value of key
print(d.keys())     # print all key
print(d.values())   # print all value
print(d.items())    # print in pair
print(d.copy())     # copy all dictionary
print(d.pop('a'))   # remove key
print(d.popitem())  # remove last pair
d.update({'f': 6})  # add or update pair
print(d)
d.update({'f': 10})  # add or update pair
print(d)
d.setdefault('g',7)  # change value
print(d)
# print(len(d))  # length of dictionary
d.update({'h': 12})
print(d) 
