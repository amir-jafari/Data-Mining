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