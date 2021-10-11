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