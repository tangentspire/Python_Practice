class Employee(object):
	"""Creates a class for an employee that has first name, last name, and
		annual salary"""
	
	def __init__(self, first_name, last_name, salary):
		"""Store first name, last name, and salary information."""
		self.first_name = first_name
		self.last_name = last_name
		self.salary = salary

	def give_raise(self, raise_amount=5000):
		"""Takes salary and gives a raise, default of 5000"""
		self.salary += raise_amount
		return self.salary
