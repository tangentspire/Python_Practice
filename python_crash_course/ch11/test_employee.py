import unittest

from employee import Employee

class TestEmployeeClass(unittest.TestCase):
	"""Tests Employee class's attribute and methods"""

	def setUp(self):
		"""
		Create a test Employee to use for unittests.
		"""
		self.first_name = 'Sean'
		self.last_name = 'Venard'
		self.salary = 40000
	
	def test_give_default_raise(self):
		"""Does the default raise of 5000 work?"""
		salary_after_raise = Employee.give_raise(self)
		self.assertEqual(salary_after_raise, 45000)

	def test_give_custom_raise(self):
		"""Does a custom raise of 10000 work?"""
		salary_after_raise = Employee.give_raise(self, 10000)
		self.assertEqual(salary_after_raise, 50000)

unittest.main()
