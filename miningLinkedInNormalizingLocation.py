import os
import csv
from collections import Counter
from operator import itemgetter
from prettytable import PrettyTable
from geopy import geocoders


GEO_APP_KEY = 'Au6TUW1p3amHYTEtblmp9WJ7ofvqFmrdHvkDdi5LKdhJWi-c0bYyInN_QZkUaptx' #bingmapsportal.com


csv_file = os.path.join('my_connections.csv')

csvReader = csv.DictReader(open(csv_file), delimiter=',', quotechar='"') #which file, seperator and valuestart/valueStop

connections = json.loads(open)

g = geocoders.Bing(GEO_APP_KEY)
#print g.geocode("Nashville", exactly_one=False)

transforms = [('Greater ', ''), (' Area', '')]

results = {}

for c in connections['values']:
	if not c.has_key('location'): continue

	transformed_location = c['location']['name']
	for transform in transforms:
		transformed_location = transformed_location.replace(*transform)

	geo = g.geocode(transformed_location, exactly_one=False)
	if geo == []: continue
	results.update( {c['location']['name'] : geo })

	print json.dumps(results, indent=1)