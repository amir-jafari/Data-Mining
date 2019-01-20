from math import sqrt
num = eval(input("Enter number: "))
root = sqrt(num);
print("Square root of", num, "=", root)
x = 16
print(sqrt(18))
print(sqrt(x))
print(sqrt(2 * x - 5))
y = sqrt(x)
print(y)
y = 2 * sqrt(x + 10) - 3
print(y)
y = sqrt(sqrt(56.0))
print(y)
print(sqrt(int('23')))
print('#',50*"-")
# -----------------------
from math import sqrt, sin, cos, pi, radians
I_x = 100
I_y = 0
Degree = 10
x, y = eval(input("Enter satellite coordinates (x,y):"))
d1 = sqrt((I_x - x)*(I_x - x) + (I_y - y)*(I_y - y))
x_old = x
x = x*(cos(radians(Degree))) - y*(sin(radians(Degree)))
y = x_old*(sin(radians(Degree))) + y*(cos(radians(Degree)))
d2 = sqrt((I_x - x)*(I_x - x) + (I_y - y)*(I_y - y))
print("Difference in distances: %.3f" % (d2 - d1))
print('#',50*"-")
# -----------------------
from time import clock
print("Enter your name: ", end="")
start_time = clock()
name = input()
elapsed = clock() - start_time
print(name, "It took you", elapsed, "seconds to type")

sum = 0
start = clock()
for n in range(1, 10001):
    sum += n
elapsed = clock() - start
print("sum:", sum, "time:", elapsed)

from time import sleep
for count in range(10, -1, -1):
    print(count)
    sleep(1)
print('#',50*"-")
# -----------------------
from time import clock
max_value = 10000
count = 0
start_time = clock()
for value in range(2, max_value + 1):
    is_prime = True
    for trial_factor in range(2, value):
        if value % trial_factor == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
print()
elapsed = clock() - start_time
print("Count:", count, " Elapsed time:", elapsed, "sec")
print('#',50*"-")
# -----------------------
from random import randrange, seed
seed(23)
for i in range(0, 100):
    print(randrange(1, 1000), end=' ')
print()
print('#',50*"-")
# -----------------------
def prompt():
    print("Please enter an integer value: ", end="")
print("This program adds together two integers.")
prompt()
value1 = int(input())
prompt()
value2 = int(input())
sum = value1 + value2
print(value1, "+", value2, "=", sum)
def count_to_n(n):
    for i in range(1, n + 1):
        print(i)
print("Going to count to five . . .")
count_to_n(5)
print('#',50*"-")
# -----------------------
def gcd(num1, num2):
    min = num1 if num1 < num2 else num2
    largestFactor = 1
    for i in range(1, min + 1):
        if num1 % i == 0 and num2 % i == 0:
            largestFactor = i
    return largestFactor
L = gcd(24, 6)
print(L)
print('#',50*"-")
# -----------------------
def increment(x):
    print("Beginning execution of increment, x =", x)
    x += 1
    print("Ending execution of increment, x =", x)
def main():
    x = 5
    print("Before increment, x =", x)
    increment(x)
    print("After increment, x =", x)
main()
print('#',50*"-")
# -----------------------
def get_input():
    global arg1, arg2
    arg1 = float(input("Enter argument #1: "))
    arg2 = float(input("Enter argument #2: "))
# -----------------------
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def main():
    # Try out the factorial function
    print(" 0! = ", factorial(0))
    print(" 1! = ", factorial(1))
    print(" 6! = ", factorial(6))
    print("10! = ", factorial(10))
main()
print('#',50*"-")
# -----------------------
'''
Contains the definition of the is_prime function
'''
from math import sqrt

def is_prime(n):
    '''
    Returns True if non-negative integer n is prime;
    otherwise, returns false
    '''
    trial_factor = 2
    root = sqrt(n)
    while trial_factor <= root:
        if n % trial_factor == 0:
            return False
    return True
print(help(is_prime))
print('#',50*"-")
# -----------------------
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[3])
nums[2] = (nums[0] + nums[9])/2;
nums[1], nums[4] = eval(input("Enter a, b: "))

collection = [1, 2, 'Amir', 19, -3, 'end']
for item in collection:
    print(item)
nums = [2, 4, 6, 8]
for i in range(len(nums) - 1, -1, -1):
    print(nums[i])
a = list(range(0, 10))
print(a)
a = list(range(10, -1, -1))
print(a)
a = list(range(0, 100, 10))
print(a)
a = list(range(-5, 6))
print(a)
print('#',50*"-")
# -----------------------
def main():
    sum = 0.0
    NUMBER_OF_ENTRIES = 5
    numbers = []
    print("Please enter", NUMBER_OF_ENTRIES, "numbers: ")
    for i in range(0, NUMBER_OF_ENTRIES):
        num = eval(input("Enter number " + str(i) + ": "))
        numbers += [num]
        sum += num

    print(end="Numbers entered: ")
    for num in numbers:
        print(num, end=" ")
    print()
    print("Average:", sum/NUMBER_OF_ENTRIES)
    print(numbers)
main()
print('#',50*"-")
# -----------------------
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
# -----------------------
lst = [10, 20, 30, 40, 50, 60, 70, 80]
print(lst)
print(lst[0:3])
print(lst[4:8])
print(lst[2:5])
print(lst[-5:-3])
print(lst[:3])
print(lst[4:])
print(lst[:])
print(lst[-100:3])
print(lst[4:100])
print('#',50*"-")
# -----------------------
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
# -----------------------
def permute(prefix, suffix):
    suffix_size = len(suffix)
    if suffix_size == 0:
        print(prefix)
    else:
        for i in range(0, suffix_size):
            new_pre = prefix + [suffix[i]]
            new_suff = suffix[:i] + suffix[i + 1:]
            permute(new_pre, new_suff)
def print_permutations(lst):
    permute([], lst)
def main():
    a = [1, 2, 3, 4]
    print_permutations(a)
main()
print('#',50*"-")
# -----------------------
a = (1, 2, 3, 4)
print(a[1])
print(a[0:3])
b = a.index(1)
print(b)
t = ("a", "b", "mpilgrim", "z", "example")
t[0]
t[-1]
# t.append("new")
v = ('a', 'b', 'e')
(x, y, z) = v
print(list(range(2)))
(MONDAY, TUESDAY, WEDNESDAY) = list(range(3))
print('#',50*"-")
# -----------------------
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
# -----------------------



