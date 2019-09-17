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