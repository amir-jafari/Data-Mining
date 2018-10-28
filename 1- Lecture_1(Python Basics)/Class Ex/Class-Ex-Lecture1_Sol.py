# =================================================================
# Class_Ex1: 

# Write python program that converts seconds to 
# (x Hour, x min, x seconds)
# ----------------------------------------------------------------
# Get the number of seconds
seconds = eval(input("Please enter the number of seconds:"))
# First, compute the number of hours in the given number of seconds
# Note: integer division with possible truncation
hours = seconds // 3600 # 3600 seconds = 1 hours
# Compute the remaining seconds after the hours are accounted for
seconds = seconds % 3600
# Next, compute the number of minutes in the remaining number of seconds
minutes = seconds // 60 # 60 seconds = 1 minute
# Compute the remaining seconds after the minutes are accounted for
seconds = seconds % 60
# Report the results
print(hours, "hr,", minutes, "min,", seconds, "sec")
# =================================================================
# Class_Ex2: 
# Write a python program to print all the different arrangements of the
# letters A, B, and C. Each string printed is a permutation of ABC.
# ----------------------------------------------------------------
for first in 'ABC':
	for second in 'ABC': # The second varies from A to C
		if second != first: # No duplicate letters allowed
			for third in 'ABC': # The third varies from A to C
				# Don't duplicate first or second letter
				if third != first and third != second:
					print(first + second + third)
# =================================================================
# Class_Ex3: 
# Write a python program to print all the different arrangements of the
# letters A, B, C and D. Each string printed is a permutation of ABCD.
# ----------------------------------------------------------------

# The first letter varies from A to D
for first in 'ABCD':
	for second in 'ABCD': # The second varies from A to D
		if second != first: # No duplicate letters allowed
			for third in 'ABCD': # The third varies from A to D
				# Don't duplicate first or second letter
				if third != first and third != second:
				for fourth in 'ABCD': The fourth varies from A to D
					if fourth != first and fourth != second and fourth != third:
						print(first + second + third + fourth)


# =================================================================
# Class_Ex4: 
# Suppose we wish to draw a triangular tree, and its height is provided 
# by the user.
# ----------------------------------------------------------------
Get tree height from user
height = eval(input("Enter height of tree: "))

# Draw one row for every unit of height
row = 0
while row < height:
	# Print leading spaces; as row gets bigger, the number of
	# leading spaces gets smaller
	count = 0
	while count < height - row:
		print(end=" ")
		count += 1

	# Print out stars, twice the current row plus one:
	# 1. number of stars on left side of tree
	# = current row value
	# 2. exactly one star in the center of tree
	# 3. number of stars on right side of tree
	# = current row value
	count = 0
	while count < 2*row + 1:
		print(end="*")
		count += 1
#	 Move cursor down to next line
	print()
	row += 1 # Consider next row
# =================================================================
# Class_Ex5: 
# Write python program to print prime numbers up to a specified values.
# ----------------------------------------------------------------
max_value = eval(input('Display primes up to what value? '))
value = 2 # Smallest prime number
while value <= max_value:
	# See if value is prime
	is_prime = True # Provisionally, value is prime
	# Try all possible factors from 2 to value - 1
	trial_factor = 2
	while trial_factor < value:
		if value % trial_factor == 0:
			is_prime = False; # Found a factor
			break # No need to continue; it is NOT prime
	trial_factor += 1 # Try the next potential factor
	if is_prime:
		print(value, end= ' ') # Display the prime number
	value += 1 # Try the next potential prime number
print() # Move cursor down to next line

# =================================================================