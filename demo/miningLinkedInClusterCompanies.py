import os
import csv
import json
from nltk.metrics.distance import jaccard_distance

CSV_FILE = os.path.join('linkedin_connections_export_microsoft_outlook.csv')

DISTANCE_THRESHOLD = 0.5
DISTANCE = jaccard_distance

def cluster_contacts_by_company(CSV_FILE):

    transforms = [(', Inc.', ''), (', Inc', ''), (', LLC', ''), (', LLP', ''), (' LLC', ''), (' Inc.', ''), (' Inc', '')]

    separators = ['/', 'and', '&']

    csvReader = csv.DictReader(open(CSV_FILE), delimiter=',', quotechar='"')
    contacts = [row for row in csvReader]

    all_titles = []
    for i, _ in enumerate(contacts):
        if contacts[i]['Company'] == '':
            contacts[i]['Company'] = ['']
            continue
        titles = [contacts[i]['Company']]
        for title in titles:
            for separator in separators:
                if title.find(separator) >= 0:
                    #titles.remove(title)
                    titles.extend([title.strip() for title in title.split(separator)
                                  if title.strip() != ''])

        for transform in transforms:
            titles = [title.replace(*transform) for title in titles]
        contacts[i]['Company'] = titles
        all_titles.extend(titles)

    all_titles = list(set(all_titles))

    clusters = {}
    for title1 in all_titles:
        clusters[title1] = []
        for title2 in all_titles:
            if title2 in clusters[title1] or clusters.has_key(title2) and title1 \
                in clusters[title2]:
                continue
            distance = DISTANCE(set(title1.split()), set(title2.split()))

            if distance < DISTANCE_THRESHOLD:
                clusters[title1].append(title2)

    # Flatten out clusters

    clusters = [clusters[title] for title in clusters if len(clusters[title]) > 1]
    print json.dumps(clusters, indent=1)
    # Round up contacts who are in these clusters and group them together

    clustered_contacts = {}
    for cluster in clusters:
        clustered_contacts[tuple(cluster)] = []
        for contact in contacts:
            for title in contact['Company']:
                if title in cluster:
                    clustered_contacts[tuple(cluster)].append('%s %s'
                            % (contact['First Name'], contact['Last Name']))

    return clustered_contacts


clustered_contacts = cluster_contacts_by_company(CSV_FILE)
#print clustered_contacts
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