# while True:
	# Do something forever. . .
MAX = 20
n = 21
while n <= MAX:
	factor = 1
	print(end=str(n) + ': ')
	while factor <= n:
		if n % factor == 0:
			print(factor, end=' ')
			factor += 1
	print()
	n += 1

MAX = 20
for n in range(1, MAX + 1):
	print(end=str(n) + ': ')
	for factor in range(1, n + 1):
		if n % factor == 0:
			print(factor, end=' ')
	print()