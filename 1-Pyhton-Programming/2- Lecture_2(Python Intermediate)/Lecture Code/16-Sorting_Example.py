from random import randrange
def random_list():
    result = []
    count = randrange(3, 20)
    for i in range(count):
        result += [randrange(-50, 50)]
    return result
def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        small = i
    for j in range(i + 1, n):
        if lst[j] < lst[small]:
            small = j
    if i != small:
        lst[i], lst[small] = lst[small], lst[i]
def main():
    for n in range(10):
        col = random_list()
        print(col)
        selection_sort(col)
        print(col)
        print('==============================')
main()
print('#',50*"-")