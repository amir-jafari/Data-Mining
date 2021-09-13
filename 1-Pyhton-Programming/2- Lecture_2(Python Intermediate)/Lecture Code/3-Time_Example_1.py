from time import time
print("Enter your name: ", end="")
start_time = time()
name = input()
elapsed = time() - start_time
print(name, "It took you", elapsed, "seconds to type")

sum = 0
start = time()
for n in range(1, 10001):
    sum += n
elapsed = time() - start
print("sum:", sum, "time:", elapsed)

from time import sleep
for count in range(10, -1, -1):
    print(count)
    sleep(1)
print('#',50*"-")