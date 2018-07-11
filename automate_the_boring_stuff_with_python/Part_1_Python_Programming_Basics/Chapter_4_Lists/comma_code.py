def transform_list_to_string(input_list):
	""" Takes a list and returns a string with the list items followed by a
	comma, the last item doesn't have a comma and is preceded by a comma. Eg. [1,
	2, 3] -> 1, 2, and 3. """
	string_list = ''
	while True:

		if len(input_list) > 1: 
			string_list += str(input_list.pop(0)) + ', ' 
			continue
		else: 
			string_list += 'and ' + input_list[-1] + '.'
			break

	print(string_list)

test_list = ['apples', 'bananas', 'tofu', 'cats']
transform_list_to_string(test_list)
