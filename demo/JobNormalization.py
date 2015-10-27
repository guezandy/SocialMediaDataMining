import os
import csv
from collections import Counter
from operator import itemgetter
from prettytable import PrettyTable

csv_file = os.path.join('linkedin_connections_export_microsoft_outlook.csv')

transforms = [
    ('Sr', 'Senior'),
    ('Sr.', 'Senior'),
    ('Jr.', 'Junior'),
    ('Jr', 'Junior'),
    ('CEO', 'Chief Executive Officer'),
    ('COO', 'Chief Operating Officer'),
    ('CTO', 'Chief Technology Officer'),
    ('CFO', 'Chief Finance Officer'),
    ('VP', 'Vice President'),
	]

csvReader = csv.DictReader(open(csv_file), delimiter=',', quotechar='"') #which file, seperator and valuestart/valueStop

contacts = [row for row in csvReader]

titles = []
for contact in contacts:
    titles.extend([t.strip() for t in contact['Job Title'].split('/')
                  if contact['Job Title'].strip() != ''])

#print titles #prints all the titles

#Replace common known abbreviations

for i, _ in enumerate(titles):
	for transform in transforms:
		titles[i] = titles[i].replace(*transform)

#print jobs

pt = PrettyTable(field_names=['Job Title', 'Freq'])
pt.align = 'l'

c = Counter(titles) #titles, freq is created here
#print c

[pt.add_row([title,freq])
for(title,freq) in sorted(c.items(), key=itemgetter(1), reverse=True)
	if freq > 1] #crashes when printing 1

print pt

token = [] #go title by title parsing words
for title in titles:
	token.extend([t.strip(',') for t in title.split()])

pt = PrettyTable(field_names=['Token','Freq'])
pt.align = 'l'
c = Counter(token)
[pt.add_row([token,freq])
for(token,freq) in sorted(c.items(), key=itemgetter(1), reverse=True)
	if freq > 1 and len(token) >2]
print pt 
