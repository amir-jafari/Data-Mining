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