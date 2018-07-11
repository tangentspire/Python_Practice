def get_number():
	try:
		number = int(input("What number would you like to call the collatz function with? > "))
		collatz(number)
	except ValueError:
		print("You have entered a non-number, please try again.")
		get_number()
		
def collatz(number):
	if 0 == (number % 2):
		number = number // 2
		print(number)
		return number	
	elif  1 == (number % 2):
		number = 3 * number + 1
		print(number)
		return number

get_number()
