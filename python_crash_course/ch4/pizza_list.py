pizzas = ['Cheese', 'Sausage', 'Spinach', 'Olive', 'Onion']

for pizza in pizzas:
	print(f"I like {pizza} pizza!")

print("I really like pizza")

print("The first three items in the list are:")
print(pizzas[:2])

print("The  three items in the middle of the list are:")
print(pizzas[1:4])

print("The last three items in the last are:")
print(pizzas[-2:])

friend_pizzas = pizzas[:]
friend_pizzas.append("Anchoives")

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas' are:")
for pizza in friend_pizzas:
    print(pizza)
