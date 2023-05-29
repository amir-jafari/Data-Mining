# x = int(input("Please enter a small positive integer: "))
# print("x =", x)
try:
    x = int(input("Please enter a small positive integer: "))
    print("x =", x)
except:
    print("Input cannot be parsed as an integer")
print('#', 50 * "-")