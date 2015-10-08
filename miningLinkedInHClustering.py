import os
import csv
import random
from nltk.metrics.distance import jaccard_distance
from cluster import HierarchicalClustering

# XXX: Place your "Outlook CSV" formatted file of connections from 
# http://www.linkedin.com/people/export-settings at the following
# location: resources/ch03-linkedin/my_connections.csv

csv_file = os.path.join('my_connections.csv')

OUT_FILE = 'd3-data.json'

# Tweak this distance threshold and try different distance calculations 
# during experimentation
DISTANCE_THRESHOLD = 0.5
DISTANCE = jaccard_distance

# Adjust sample size as needed to reduce the runtime of the
# nested loop that invokes the DISTANCE function
SAMPLE_SIZE = 500

def cluster_contacts_by_title(csv_file):

    transforms = [
        ('Sr.', 'Senior'),
        ('Sr', 'Senior'),
        ('Jr.', 'Junior'),
        ('Jr', 'Junior'),
        ('CEO', 'Chief Executive Officer'),
        ('COO', 'Chief Operating Officer'),
        ('CTO', 'Chief Technology Officer'),
        ('CFO', 'Chief Finance Officer'),
        ('VP', 'Vice President'),
        ]

    separators = ['/', 'and', '&']

    csvReader = csv.DictReader(open(csv_file), delimiter=',', quotechar='"')
    contacts = [row for row in csvReader]

    # Normalize and/or replace known abbreviations
    # and build up list of common titles

    all_titles = []
    for i, _ in enumerate(contacts):
        if contacts[i]['Job Title'] == '':
            contacts[i]['Job Titles'] = ['']
            continue
        titles = [contacts[i]['Job Title']]
        for title in titles:
            for separator in separators:
                if title.find(separator) >= 0:
                    #titles.remove(title)
                    titles.extend([title.strip() for title in title.split(separator)
                                  if title.strip() != ''])

        for transform in transforms:
            titles = [title.replace(*transform) for title in titles]
        contacts[i]['Job Titles'] = titles
        all_titles.extend(titles)

    all_titles = list(set(all_titles))
    
    # Define a scoring function
    def score(title1, title2): 
        return DISTANCE(set(title1.split()), set(title2.split()))

    # Feed the class your data and the scoring function
    hc = HierarchicalClustering(all_titles, score)

    # Cluster the data according to a distance threshold
    clusters = hc.getlevel(DISTANCE_THRESHOLD)

    # Remove singleton clusters
    clusters = [c for c in clusters if len(c) > 1]

    # Round up contacts who are in these clusters and group them together

    clustered_contacts = {}
    for cluster in clusters:
        clustered_contacts[tuple(cluster)] = []
        for contact in contacts:
            for title in contact['Job Titles']:
                if title in cluster:
                    clustered_contacts[tuple(cluster)].append('%s %s'
                            % (contact['First Name'], contact['Last Name']))

    return clustered_contacts

def display_output(clustered_contacts):
    
    for titles in clustered_contacts:
        common_titles_heading = 'Common Titles: ' + ', '.join(titles)

        descriptive_terms = set(titles[0].split())
        for title in titles:
            descriptive_terms.intersection_update(set(title.split()))
        descriptive_terms_heading = 'Descriptive Terms: ' \
            + ', '.join(descriptive_terms)
        print descriptive_terms_heading
        print '-' * max(len(descriptive_terms_heading), len(common_titles_heading))
        print '\n'.join(clustered_contacts[titles])
        print

def write_d3_json_output(clustered_contacts):
    
    json_output = {'name' : 'My LinkedIn', 'children' : []}

    for titles in clustered_contacts:

        descriptive_terms = set(titles[0].split())
        for title in titles:
            descriptive_terms.intersection_update(set(title.split()))

        json_output['children'].append({'name' : ', '.join(descriptive_terms)[:30], 
                                    'children' : [ {'name' : c.decode('utf-8', 'replace')} for c in clustered_contacts[titles] ] } )
    
        f = open(OUT_FILE, 'w')
        f.write(json.dumps(json_output, indent=1))
        f.close()
    
clustered_contacts = cluster_contacts_by_title(csv_file)
display_output(clustered_contacts)
write_d3_json_output(clustered_contacts)