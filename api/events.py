import requests
import credentials
import json
from collections import OrderedDict
from defaults import *
user = {}

def get_zip():
	"""
	Get the zip code of the user, find nearest 10 zipcodes.
	"""
	# prompt for ZIP code
	# on response, check if valid 5-digit ZIP code
	# if not, try again
	zipcode = input('Enter your zip code: ')
	user['zipcode'] = zipcode

	# save their zipcode
	# search for nearby zip code with geonames API
	# save top 5 nearby zip codes.
	url = 'http://api.geonames.org/findNearbyPostalCodesJSON?postalcode=%d&country=US&radius=30&username=%s&maxRows=10' % (zipcode, credentials.geonames['username'])
	response = json.loads(requests.get(url).content)['postalCodes']
	zipcodes = [location['postalCode'] for location in response]

	user['zipcodes'] = zipcodes

def find_nearest_libraries(zipcodes=None):
	"""
	Finds the (up to) nearest 5 libraries by searching locations for matching nearest zip codes.
	"""
	if not zipcodes:
		zipcodes = user['zipcodes']
	# search libraries to see if its zipcode is in zipcodes
	nearby = []
	for library in libraries:
		if library['zipcode'] in zipcodes:
			nearby.append(library)

	nearest = []
	for zipcode in zipcodes:
		for library in nearby:
			if library['zipcode'] == zipcode:
				# Remove library from nearby, place in nearest.
				nearby.remove(library)
				nearest.append(library)

	user['libraries'] = nearest

	return nearest

def get_days_of_week():
	"""
	Get the days of week that the person is most free.
	Any day.
	Weekends only.
	Certain days of week.
	"""
	message = "Which days do you want to get event updates for?\n"
	options = OrderedDict((
		("1","Just weekends."),
		("2","Just weekdays."),
		("3","Any day of the week.")))
	print options
	days = {
		"1" : ['Saturday', 'Sunday'],
		"2" : ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday'],
		"3" : ['Monday','Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
	}
	message += '\n'.join('%s: %s' %(number, label) for (number, label) in options.iteritems()) + '\n'
	# on response, check if options has key.
	# if not, try again.
	preferredDays = input(message)
	# save their preferred days of the week.
	user['preferredDays'] = days[str(preferredDays)]

def find_events():
	"""
	Using days of week and nearest libraries, searches for future events.
	"""

def remind_user():
	"""
	Reminds user of upcoming events.
	"""

if __name__ == '__main__':
	get_zip()
	find_nearest_libraries()
	get_days_of_week()
	print user.keys()
	print user['preferredDays']
	print user['zipcodes']
	print [library['facility_name'] for library in user['libraries']]
	