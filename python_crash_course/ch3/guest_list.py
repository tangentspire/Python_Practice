guests = ['Seneca', 'Cato the Younger', 'Gaius Julius']

def print_guestlist(the_list):
	for guest in guests:
		print(f"Welcome to dinner, {guest}, it is a pleasure to have you.")

print_guestlist(guests)

print("Seneca cannot make the dinner.")
guests.remove('Seneca')
print("I'll invite Pompei instead!")
guests.insert(0, 'Pompei')

print_guestlist(guests)
print("I have found a bigger table.")
guests.insert(0, 'Brutus')
guests.insert(round(len(guests)/2), 'Pliny the Elder')
guests.append('Cicerio')
print(guests)
print_guestlist(guests)
print("Actually I can only invite two of you to dinner.")

while len(guests) > 2:
	sorry_guest = guests.pop(0)
	print(f"I am so sorry {sorry_guest}.")

print(guests)

for guest in guests:
	print(f"{guest}, you are still invited see you there!")


print(guests)

