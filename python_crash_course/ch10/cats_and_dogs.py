filename = input("Please provide the filename you would like to print out. > ")

try:
	with open(filename) as printfile:
		contents = printfile.readlines()
		for line in contents:
			print(line.rstrip())	
except FileNotFoundError:
	pass
