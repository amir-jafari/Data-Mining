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