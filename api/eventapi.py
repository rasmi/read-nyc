# eventapi.py

from bs4 import BeautifulSoup
import requests
from defaults import daysofweek
from datetime import date

def build_url(args):
	base_url = 'http://www.nypl.org/events/classes/calendar?'

	if not 'date1' in args:
		today = date.today()
		args['date1'] = str(today.month) + '/' + str(today.day) + '/' + str(today.year)

	url = base_url + \
		'keyword=' + args['keyword'] + \
		'&location=' + args['location'] + \
		'&topic=' + args['topic'] + \
		'&audience=' + args['audience'] + \
		'&date_op=' + args['date_option'] + \
		'&date1=' + args['date1']

	if 'date2' in args:
		url += '&date2=' + args['date2']

	return url

def make_event(eventData):
    time = eventData[0].text
    name = eventData[1].text
    location = eventData[2].text
    audience = eventData[3].text.split(',')
    event = {'time': time, 'name': name, 'location': location, 'audience': audience}

    return event

#testurl = 'http://www.nypl.org/events/classes/calendar?keyword=&location=46&topic=&audience=&series=&date_op=GREATER_EQUAL&date1=09%2F04%2F2014'
#url = 'http://www.nypl.org/events/classes/calendar?keyword=&location=&topic=&audience=&series=&date_op=GREATER_EQUAL&date1=08%2F20%2F2014'

def get(url):
	r = requests.get(url)
	table = BeautifulSoup(r.text).find('table')

	rows = table.find_all('tr')

	events = []

	day = ''

	for row in rows:
		eventData = row.find_all('td')
		
		if len(eventData) == 4:
			event = make_event(eventData)
			event['day'] = day
			events.append(event)
		else:
			daytext = row.text.split(', ')[0]
			if daytext in daysofweek:
				day = daytext

	for event in events:
		print event['day'] + ": " + event['name']
	#print len(events)

def get_events(args):
	url = build_url(args)
	events = get(url)
	return events
