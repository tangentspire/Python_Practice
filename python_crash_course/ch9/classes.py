class Restaurant(object):
	""" Models a restaurant """
	def	__init__(self, restaurant_name, cuisine_type):
			self.restaurant_name = restaurant_name
			self.cuisine_type = cuisine_type
			self.number_served = 0
	
	def describe_restaurant(self):
		print(self.restaurant_name)
		print(self.cuisine_type)

	def open_restaurant(self):
		print(f"The restaurant {self.restaurant_name} is now open")	
	
	def set_number_served(self, number_served):
		self.number_served = number_served
		print(self.number_served)


restaurant = Restaurant('Sushi House', 'Japanese')
italian_restaurant = Restaurant('Pasta Party', 'Italian')
greek_restaurant = Restaurant('Pantheon', 'Greek')

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(100)

italian_restaurant.describe_restaurant()
italian_restaurant.open_restaurant()

greek_restaurant.describe_restaurant()
greek_restaurant.describe_restaurant()
