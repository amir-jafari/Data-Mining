def printall(*args):
    print (args)
printall(1, 2.0, '3')
t = (7, 3)
# divmod(t) --->Wrong
divmod(*t)
s = 'abc'
t = [0, 1, 2]
print(zip(s, t))
print(zip('Anne', 'Elk'))
print('#',50*"-")