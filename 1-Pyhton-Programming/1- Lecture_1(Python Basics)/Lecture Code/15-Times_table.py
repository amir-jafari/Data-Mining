print(" 1 2 3 4 5 6 7 8 9 10")
print(" +----------------------------------------")
for row in range(1, 11):
	if row < 10:
		print(" ", end="")
	print(row, "| ", end="")
	for column in range(1, 11):
		product = row*column
		if product < 100:
			print(end=" ")
		if product < 10:
			print(end=" ")
		print(product, end=" ")
	print()