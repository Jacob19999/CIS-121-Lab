def count_duplicates(num_1, num_2, num_3):
	count = 0
	
	# if we have 3 numbers 1,2,3
	# we check if first number == second number
	# We check if first number == third number
	# We check if second number == third number

	if num_1 == num_2:
		count += 1
	
	if num_1 == num_3:
		count += 1

	if num_2 == num_3:
		count += 1
	
	if count == 0:
		return "Each number is unique"
	elif count == 3:
		return "You entered the same number 3 times"
	else:
		return "You entered the same number 2 times"