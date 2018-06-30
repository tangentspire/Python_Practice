import json

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username

def greet_user():
	"""Greet the user by name."""
	username = get_stored_username()
	if username:
		print(f"Hello {username}!")
		correct_username = input("Is this the correct username? Yes or No > ")
		correct_username = correct_username.lower()
		if correct_username == 'no':
			username = input("What is your name? > ")
			filename = 'username.json'
			with open(filename, 'w') as f_obj:
				json.dump(username, f_obj)
		elif correct_username == 'yes':
			print(f"Hello {username}!")
		else:
			greet()					

		print("We'll remember you when you come back, " + username + "!")

greet_user()
