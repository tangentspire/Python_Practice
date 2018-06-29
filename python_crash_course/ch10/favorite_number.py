import json

def get_number():
	"""Asks user for favorite number and stores it."""
	favorite_number = input("What is your favorite number? > ")
	return favorite_number
				
def store_number():
	"""Stores the users favorite number in a .json file"""
	
	try:
		with open(number_file) as f_obj:
			json.dump(
