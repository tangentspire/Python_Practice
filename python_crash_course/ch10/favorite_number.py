import json

def get_number():
	"""Asks user for favorite number and stores it."""
	favorite_number = input("What is your favorite number? > ")
	return favorite_number
				
def store_number():
	"""Stores the users favorite number in a .json file"""
	filename = 'favorite_number.json'
	with open(filename, 'w') as f_obj:
		json.dump(get_number(), f_obj)

def fetch_number():
	"""Fetches the user's favorite number in the .json file."""
	filename = 'favorite_number.json'
	with open(filename) as f_obj:
		favorite_number = json.load(f_obj)
	return favorite_number

def print_number():
	"""Prints the user's favorite number from the .json file."""
	favorite_number = fetch_number()
	print(f"Your favorite number is {favorite_number}!")

def favorite_number():
	"""Checks if the user has already stored their favorite number and prints
	   if the .json file exists if not it asks for user's favorite number"""
	try:
		print_number()
	except FileNotFoundError:
		store_number()
		print_number()
			

favorite_number()
