filename = 'learning_python.txt'
with open(filename) as file_object:
	file_contents = file_object.readlines()
	print(file_contents)

for line in file_contents:
	print(line.rstrip())

line_list = []

for line in file_contents:
	line_list.append(line)

print(line_list)

message = "In Python, you can do anything."
print(message.replace('Python', 'C'))
