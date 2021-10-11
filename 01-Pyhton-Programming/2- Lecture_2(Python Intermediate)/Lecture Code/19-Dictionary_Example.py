d = {"server":"one","database":"master"}
d["database"]
d["database"] = "pubs"
d["uid"] = "sa"
d["retrycount"] = 3
d[42] = "douglas"
del d[42]
d.clear()
empty_dict = {}
my_dict = {'a': 1, 'b': 2, 'c': "3"}
print(my_dict['a'])
del my_dict['b']
print(my_dict.get('e'))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
print('c' in my_dict)
print('#',50*"-")