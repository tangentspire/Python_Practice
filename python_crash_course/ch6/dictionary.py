person_dict = {
        'first_name' : "Sean",
        'last_name' : "Venard",
        'age' : 28,
        'city' : "Palo Alto"
        }

print(person_dict['first_name'])
print(person_dict['last_name'])
print(person_dict['age'])
print(person_dict['city'])


favorite_number = {
        'Sean' : 5,
        'Claire' : 4,
        'Bridget' : 13,
        'Tyler' : 666,
        'Bill' : 6
        }

for number in favorite_number:
    print(f"{number}'s favorite number is {favorite_number[number]}.")


glossary = {
        'list' : 'An object that holds an ordered collection of other objects',
        'variable' : 'An object that holds values.', 
        'dictionary' : 'A list of key pairs two pieces of information linked.', 
        'loops' : 'Syntax that repeatedly does an action until stopped.',
        'error' : 'computer doesn\'t know what to do or is surprised.'
        }

for word in glossary:
    print(f"\n{word} :  {glossary[word]}")
