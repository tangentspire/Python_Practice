filename = 'guest.txt'

with open(filename, 'a') as file_object:
	while True: 
		name = input("Please input your name. > ")
		if name == 'quit':
			break
		else:
			file_object.write(f"{name} \n")
