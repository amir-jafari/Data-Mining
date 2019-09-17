a = [1, 2, 3, 4]
b = [1, 2, 3, 4]
print('Is ', a, ' equal to ', b, '?', sep='', end=' ')
print(a == b)
print('Are ', a, ' and ', b, ' aliases?', sep='', end=' ')
print(a is b)
c = [10, 20, 30, 40]
d = c
print('Is ', c, ' equal to ', d, '?', sep='', end=' ')
print(c == d)
print('Are ', c, ' and ', d, ' aliases?', sep='', end=' ')
print(c is d)
print('#',50*"-")