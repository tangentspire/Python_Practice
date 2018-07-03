def combine_city_country(city, country, population=''):
	"""Takes city and country and combines them into a single string"""
	if population:
		city_country = city + ', ' + country + ' - ' + 'population ' + str(population)
		return city_country
	else:
		city_country = city + ', ' + country
		return city_country
