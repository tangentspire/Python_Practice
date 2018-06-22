current_users = ['Bill', 'Eric', 'John', 'George', 'Will']
new_users = ['Jim', 'BILL', 'Eric', 'Daniel', 'Sean']
current_users_lowercase = [current_user.lower() for current_user in current_users] 
new_users_lowercase = [new_user.lower() for new_user in new_users]

for new_user in new_users_lowercase:
	if new_user in current_users_lowercase:
		print(f"I am sorry, {new_user} is already taken.")
	else:
		print(f"Congratulations {new_user}, you have been added to the system!")
	

