count = 0
while count <= 3:
	print(count)
	count += 1
entry = 0
sum = 0
print("Enter numbers to sum, negative number ends list:")
while entry >= 0:
	entry = int(input())
	if int(entry) >= 0:
		sum += int(entry)
print("Sum =", sum)
n = 1
stop = int(input())
while n <= stop:
	print(n)
	n += 1