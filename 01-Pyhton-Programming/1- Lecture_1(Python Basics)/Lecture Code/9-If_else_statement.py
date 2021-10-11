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