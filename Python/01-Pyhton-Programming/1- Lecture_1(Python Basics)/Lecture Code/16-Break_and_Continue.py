entry = 0
sum = 0
print("Enter numbers to sum, negative number ends list:")
while True:
	entry = eval(input())
	if entry < 0:
		break
	sum += entry
print("Sum =", sum)

sum = 0
done = False
while not done:
	val = eval(input("Enter positive integer (999 quits):"))
	if val < 0:
		print("Negative value", val, "ignored")
		continue
	if val != 999:
		print("Tallying", val)
		sum += val
	else:
		done = (val == 999)
print("sum =", sum)