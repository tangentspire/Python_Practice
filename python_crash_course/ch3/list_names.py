names = ['Sean', 'John', 'Mike']
print(names[0])
print(names[1])
print(names[2])

print(f"I am sorry {names[0]}, I can't let you do that.")
print(f"I am sorry {names[1]}, I can't let you do that.")
print(f"I am sorry {names[2]}, I can't let you do that.")

airplanes = ['BF-109', 'FW-190', 'P-47', 'P-40', 'Spitfire', 'AM6 Zero']
for airplane in airplanes:
	print(f"I would love to own a {airplane}")

airplanes_popped = []

while len(airplanes) > 0: 
	print(f"I would love to own a {airplanes[0]}.")
	airplanes_popped.append(airplanes.pop(0))
print(airplanes)
airplanes = airplanes_popped
print(airplanes)


