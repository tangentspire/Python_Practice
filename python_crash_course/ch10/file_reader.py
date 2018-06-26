# read file from in current directory
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
	print(contents.rstrip())

file_name = 'pi_digits.txt'

# same as above but just using a variable to hold the name of the file
with open(file_name) as file_object:
	for line in file_object:
		print(line.rstrip())

file_path = '/Users/svernard/Python/Python_Practice/README.md'

# Reads a file from an absolute path
with open(file_path) as file_object:
	for line in file_object:
		print(line.rstrip())

file_path_2 = 'test_dir/test_file.txt'

# opens a file from a relative path, specifically goes down a directory and
# specifies the file
with open(file_path_2) as file_object:
	for line in file_object:
		print(line.rstrip())

with open('pi_digits.txt') as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.rstrip())
