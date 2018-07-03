import unittest 
from city_functions import combine_city_country

class CityTestCase(unittest.TestCase):
	"""Tests for 'city_functions.py'"""
	
	def test_combine_city_country(self):
		""" Do cities like santiago and countries like Chile work?"""
		formatted_name = combine_city_country('Santiago', 'Chile')
		self.assertEqual(formatted_name, 'Santiago, Chile')
	
	def test_combine_city_country_population(self):
		"""Do cities, countrys, and population like: Santiago, Chile 50000
			work? """
		formatted_name = combine_city_country('Santiago', 'Chile',
														50000)
		self.assertEqual(formatted_name, "Santiago, Chile - population 50000")

unittest.main()
