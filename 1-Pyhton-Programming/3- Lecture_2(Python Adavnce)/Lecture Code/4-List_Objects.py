t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
print(t1.extend(t2));print(t2)
t = ['d', 'c', 'e', 'b', 'a']
print(t.sort()); print(t)
def add_all(t):
    total = 0
    for x in t:
        total += x
    return total
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
t = ['a', 'b', 'c']
x = t.pop(1); print(t)
s = 'spam'
print(list(s))
s = 'spam-spam-spam'
print(s.split('-')); print(s)
t = ['I', 'Love', 'Python', 'Very Much']
delimiter = ' '
print(delimiter.join(t))
print('#',50*"-")