print("Give me two numbers and I'll add them.")
print("Enter 'q' to quit.")

while True:

	first_number = input("\nPlease enter the first number > ")
	if first_number == 'q':
		break
	second_number = input("Please enter the second number > ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) + int(second_number)		
	except ValueError:
		print("Please only input integer values.")
	else:
		print(f"If you add {first_number} and {second_number} you get {answer}.")	
