from time import time
max_value = 10000
count = 0
start_time = time()
for value in range(2, max_value + 1):
    is_prime = True
    for trial_factor in range(2, value):
        if value % trial_factor == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
print()
elapsed = time() - start_time
print("Count:", count, " Elapsed time:", elapsed, "sec")
print('#',50*"-")