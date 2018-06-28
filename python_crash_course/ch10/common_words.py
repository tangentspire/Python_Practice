filename = input("Which file would you like to count words in? > ")
word = input("What word would you like to count? > ")

with open(filename) as inputfile:
	contents = inputfile.read()
	print(f"The word '{word}' appears {contents.count(word)} times")
