# Open and store the secret password in a variable.
with open('SecretPasswordFile.txt') as f_obj:
	secret_password = f_obj.read()
	#Strips the \n from
	secret_password = secret_password.strip()

password_attempts = 1
allowed_attempts = 3
# Evaluate the inputed password
# TODO: Make a function that returns how many password attempts the user still
# has . 
while True:

	typed_password = input("Enter your password, please > ")
	print(f"You have {allowed_attempts - password_attempts} password attempts remaining.")

	if password_attempts >  allowed_attempts:
		print("You have exceeded the maximum number of password attempts. Goodbye.")
		break
	elif typed_password == secret_password:
		print('Access granted')
		break
	elif typed_password == '12345':
		print("That password is one that an idiot puts on their luggage.")
		password_attempts += 1
		continue
	else:
		print('Incorrect Password: Access denied')
		password_attempts += 1
		continue
# Takes the global variables password_attempts and allowed attempts and returns
# them after every attempt at a password. 
def return_password_attempts():
	password_attempts += 1
	allowed_attempts -= 1			
	
	return password_attempts
	return allowed_attempts	

return_password_attempts()

print(f"This is the number of password attempts remaining from the function. {password attempts}.")

print(f"This is the number of allowed_attempts remaining from the function. {allowed_attempts}")

