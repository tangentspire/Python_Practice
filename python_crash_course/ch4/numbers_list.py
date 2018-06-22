def number_printer(list):
	for number in numbers:
		print(number)

numbers = range(1, 21)

number_printer(numbers)

numbers = range(1, 1000001)

number_printer(numbers)

print(min(numbers))

print(max(numbers))

sum(numbers)

odd_numbers = range(1, 20, 2)

number_printer(odd_numbers)

three_numbers = range(3, 30, 3)

number_printer(three_numbers)

cubes = [value ** 3 for value in range(1, 11)]

number_printer(cubes)
