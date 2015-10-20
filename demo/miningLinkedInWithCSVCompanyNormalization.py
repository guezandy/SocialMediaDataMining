#log into linkedin go to connectiong
#hit settings
#export linkedin in connections
#download CSV
#open csv

#NORMALIZE

#1. Normalize and count companies:
import os
import csv
from collections import Counter
from operator import itemgetter
from prettytable import PrettyTable

csv_file = os.path.join('linkedin_connections_export_microsoft_outlook.csv')
#google vs google Inc vs google coporation
#LLC
#LLP
#INC
#transforms = [];
transforms = [(' Company',''),(' Co.',''), (' Co',''), (', Inc.', ''), (', Inc', ''), (', LLC', ''), (', LLP', ''), (' LLC', ''), (' Inc.', ''), (' Inc', '')]

csvReader = csv.DictReader(open(csv_file), delimiter=',', quotechar='"') #which file, seperator and valuestart/valueStop

contacts = [row for row in csvReader]

companies = [c['Company'].strip() 
for c in contacts 
	if c['Company'].strip() != '']

for i, _ in enumerate(companies): 
	for transform in transforms:
		companies[i] = companies[i].replace(*transform)

# f(*args) = f(1,7) as long as args = [1,7]

#print companies

pt = PrettyTable(field_names=['Company', 'Freq'])
pt.align = 'l'

c = Counter(companies) #company, freq is created here
#print c

[pt.add_row([company,freq])
for(company,freq) in sorted(c.items(), key=itemgetter(1), reverse=True)
	if freq > 1] #crashes when printing 1

print pt