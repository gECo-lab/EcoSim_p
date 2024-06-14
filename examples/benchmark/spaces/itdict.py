# iterate over two dicitionaries as stacks 

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'x': 10, 'y': 20, 'z': 30}

for key1, key2 in zip(reversed(dict1), reversed(dict2)):
    value1 = dict1[key1]
    value2 = dict2[key2]
    # Do something with value1 and value2
    print(value1, value2)