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