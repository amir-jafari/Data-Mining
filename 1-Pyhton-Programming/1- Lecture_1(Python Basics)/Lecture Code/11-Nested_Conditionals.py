value = eval(input("Enter value in the range 0 to10: "))
if int(value) >= 0: # First check
	if int(value) <= 10:
		print("In range")
print("Done")
value = eval(input("Enter value in the range 0 to10: "))
if int(value) >= 0 and int(value) <= 10:
	print("In range")
print("Done")