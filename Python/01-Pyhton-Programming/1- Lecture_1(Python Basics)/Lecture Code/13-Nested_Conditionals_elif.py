value = eval(input("Enter a value from range 0 to 5: "))
if int(value) < 0:
	print("Too small")
elif int(value) == 0:
	print("zero")
elif int(value) == 1:
	print("one")
elif int(value) == 2:
	print("two")
elif int(value) == 3:
	print("three")
elif int(value) == 4:
	print("four")
elif int(value) == 5:
	print("five")
else:
	print("Too large")
print("Done")