from random import randrange, seed
seed(23)
for i in range(0, 100):
    print(randrange(1, 1000), end=' ')
print()
print('#',50*"-")