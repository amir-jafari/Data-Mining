1 + 2 + 4 + 10 + 3
print(1 + 2 + 4 + 10 + 3)
print(10)
print("10")
print('10')
print("Amir")
print('Amir')
# print(Amir)---> Error
print(type(4))
print(type("4"))
print(str(4))
print(int('5'))
# int("Hi")---> Error
print('5' + "10")
print('abc' + 'efg')
# print(5 + '10') ---> Error
print(2 + int('11'))
# %%--------------------
x = 2
print(x)
print('x')
# 5 = x
print('x = ' + str(x))
x = 20
print('x = ' + str(x))
x , y, z = 20, 40, -30
print('x =', x, ' y =', y, ' z =', z)
a = 1
print('First, variable a has value', a,
                       'and type', type(a))
a = 'abc'
print('Now, variable a has value', a,
                       'and type', type(a))
# %%--------------------
x = 5.62
print(type(x))
pi = 3.14159
print("Pi =", pi)
print("or", 3.14, "short")
avogadros_number = 6.022e23
c = 2.998e8
print("Avogadro's number =", avogadros_number)
print("Speed of light =", c)
# %%--------------------
print('A\nB\nC')
print('D\tE\tF')
print('WX\bYZ') #---> Backspace
print('1\a2\a3\a4\a5\a6') #---> Alert
print("Did you know that 'word' is a word?")
print('Did you know that "word" is a word?')
print('Did you know that \'word\' is a word?')
print("Did you know that \"word\" is a word?")
filename = 'C:\\Users\\rick'
print(filename)
# %%--------------------
print('Please enter your First Name: ')
x = input()
print('Text entered:', x)
print('Type:', type(x))
print('Please enter an integer value:')
x = input()
print('Please enter another integer value:')
y = input()
w, x, y, z = 10, 15, 20, 25
print(w, x, y, z)
print(w, x, y, z, sep=',')
print(w, x, y, z, sep='')
print(w, x, y, z, sep=':')
print(w, x, y, z, sep='-----')
# # %%--------------------
x, y, z = 3, -4, 0
x = -x
y = -y
z = -z
print(x, y, z)
x = +y
print(x)
print(10/3, 3/10, 10//3, 3//10)
print(10%3, 3%10)
# # %%--------------------
degreesF = eval(input('Enter the temperature in degrees F: '))
# Perform the conversion
degreesC = 5/9*(degreesF - 32)
# Report the result
print('temperature in degrees C: ', degreesC)
# %%--------------------
a = True
b = False
print('a =', a, ' b =', b)
a = False;
print('a =', a, ' b =', b)
dividend, divisor = eval(input('Enter two numbers to divide: '))
if int(divisor) != 0:
	print('dividend / divisor = ', int(dividend)/int(divisor))
if x < 1:
	y = x
if x < 1: y = x
dividend, divisor = eval(input('Please enter two numbers: '))
if int(divisor) != 0:
	quotient = int(dividend)/int(divisor)
	print(str(dividend) + '/'+ str(divisor) + "=", quotient)
print('Program finished')
# %%--------------------
dividend, divisor = eval(input('Please enter two numbers: '))
if int(divisor) != 0:
	print(str(dividend)+ '/'+ str(divisor)+ "=", int(dividend)/int(divisor))
else:
	print('Division by zero is not allowed')
a1 = 1 - 1
a2 = 2 - 2
print('a1 =', a1, ' a2 =', a2)
if a1 == a2:
	print('They are Same.')
else:
	print('They are Different.')
# %%--------------------
x = 1
y = 2
b = (x == 1) 
b = (x != 1) 
b = (x == 1 and y == 2) 
b = (x != 1 and y == 2) 
b = (x == 1 and y != 2) 
b = (x != 1 and y != 2) 
b = (x == 1 or y == 2) 
b = (x != 1 or y == 2) 
b = (x == 1 or y != 2) 
b = (x != 1 or y != 2)
if x == 1 or 2 or 3:
	print("OK") 
x == 1 or 2 or 3
# %%--------------------
value = eval(input("Enter value in the range 0 to10: "))
if int(value) >= 0: # First check
	if int(value) <= 10:
		print("In range")
print("Done")
value = eval(input("Enter value in the range 0 to10: "))
if int(value) >= 0 and int(value) <= 10:
	print("In range")
print("Done")
# %%--------------------
print("Help! My computer doesn't work!")
print("Does the computer make any sounds (fans, etc.)")
choice = input("or show any lights? (y/n):")
if choice == 'n': 
	choice = input("Is it plugged in? (y/n):")
	if choice == 'n': 
		print("Plug it in. If the problem persists, ")
		print("please run this program again.")
	else:
		choice = input("Is switch in \"on\" position?(y/n):")
		if choice == 'n':
			print("Turn it on. If the problem persists, ")
			print("please run this program again.")
		else: 
			choice = input("Does it have a fuse?(y/n):")
			if choice == 'n': 
				choice = input("Is the outlet OK? (y/n):")
				if choice == 'n': 
					print("Check the outlet's circuit ")
					print("breaker or fuse. Move to a")
					print("new outlet, if necessary. ")
					print("If the problem persists, ")
					print("please run this program again.")
				else: 
					print("Consult a service technician.")
			else: 
				print("Check the fuse. Replace if ")
				print("necessary. If the problem ")
				print("persists, then ")
				print("please run this program again.")
else:
	print("Please consult a service technician.")
# %%--------------------
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
# %%--------------------
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
# %%--------------------
for n in range(1, 11):
	print(n)
for n in range(21, 0, -3):
	print(n, '', end='')
sum = 0 
for i in range(1, 100):
	sum += i
print(sum)
# %%--------------------
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
# %%--------------------
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
# %%--------------------
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
# %%--------------------
val = eval(input('Enter number: '))
root = 1.0;
diff = root*root - val
while diff > 0.00000001 or diff < -0.00000001:
	root = (root + val/root) / 2 
	print(root, 'squared is', root*root) 
	diff = root*root - val
print('Square root of', val, "=", root)
# %%--------------------






