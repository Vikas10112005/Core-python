dict_example = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("Original dictionary:", dict_example)
# dict_example.clear()
#print("Dictionary after clear():", dict_example)

dict_copy = dict_example.copy()
#print("Dictionary copy:", dict_copy)



keys = ['e', 'f', 'g']
default_value =0
new_dict =dict.fromkeys(keys, default_value)
# print('New dictionary with fromkeys():', new_dict)
#
#
#
# print("Value for key 'b':", dict_example.get('b'))  # Output: 2
# print("Dictionary items:", dict_example.items())
print("Dictionary keys:", dict_example.keys())


# popped_value = dict_example.pop('b')
# print("Popped value for key 'b':", popped_value)
# print("Dictionary after pop():", dict_example)



# last_item = dict_example.popitem()
# print("Popped last item:", last_item)
# print("Dictionary after popitem():", dict_example)


# print("Value for key 'z' with setdefault:", dict_example.setdefault('z', 100))
# print("Dictionary after setdefault():", dict_example)

# new_data = {'x': 10, 'y': 20}
# dict_example.update(new_data)
# print("Dictionary after update():", dict_example)


print("Dictionary values:", dict_example.values())