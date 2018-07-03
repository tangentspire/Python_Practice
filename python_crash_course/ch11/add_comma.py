filename = 'emails.txt'

with open(filename, 'w') as f_obj:
	email_list = f_obj.readline()
	for email in email_list:
		new_email = email + ', '			
		
