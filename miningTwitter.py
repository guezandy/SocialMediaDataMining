#twitter is considered an interest graph see page 45 bottom for more info


import twitter
import json
from collections import Counter
from prettytable import PrettyTable

CONSUMER_KEY = 'oh1w3vI78yB9b4UtQGZs8ToMW'
CONSUMER_SECRET = 'KUiKSRCAJ7DTv7Gsd7Az6rMWxtNemJ7ggYwR2lTh38A8w8ZKGs'
OAUTH_TOKEN = '1456118952-AIZUwLj9WQAvKRpKFxVR7GoKMuUQusIw9M48Emk'
OAUTH_TOKEN_SECRET = 'VbKe40gacRME1KA7FgBTL4whO4Q54BT3iXKgANLkyd3bZ'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
#twitter_api = twitter.Api(consumer_key='CONSUMER_KEY',
                     # consumer_secret='CONSUMER_SECRET',
                     # access_token_key='OAUTH_TOKEN',
                     # access_token_secret='OAUTH_TOKEN_SECRET')

twitter_api = twitter.Twitter(auth=auth)

print twitter_api

# trending topics 1 equals the whole world
WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

#print world_trends
#print json.dumps(world_trends, indent=1)
#print
#print json.dumps(us_trends, indent=1)

#find where world and us trends intersect

world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])
us_trends_set = set([trend['name'] for trend in us_trends[0]['trends']])

#print us_trends_set

common_trends = world_trends_set.intersection(us_trends_set)
print common_trends

#topic to search twitter about

q = 'Software'
count = 100
search_results = twitter_api.search.tweets(q=q, count=count)
statuses = search_results['statuses']

#iterate through 5 more batches of tweets
for _ in range(5):
	#print "Length of status", len(statuses)
	try: 
		next_results = search_results['search_metadata']['next_results']
	except KeyError, e: #no more results so break
		break
	#create a dictionaty with the results
	kwargs = dict([ kv.split('=') for kv in next_results[1:].split("&")])
	search_results = twitter_api.search.tweets(**kwargs)
	statuses += search_results['statuses']


	#for x in range(0, 10):
	#	print json.dumps(statuses[x]['text'], indent=1)



#get text of tweet
status_texts = [status['text'] for status in statuses]

#get names of person tweeting
screen_names = [ user_mention['screen_name'] for status in statuses for user_mention in status['entities']['user_mentions']]

#get hashtags per post
hashtags = [ hashtag['text'] for status in statuses for hashtag in status['entities']['hashtags']]

#get all the words in the tweets
words = [w for t in status_texts for w in t.split()]

#print the first 5 of each
print 'First 5 text in status'
print json.dumps(status_texts[0:5], indent=1)
#print 'First 5 screen names'
print json.dumps(screen_names[0:5], indent=1)
#print 'First 5 hashtags'
print json.dumps(hashtags[0:5], indent=1)
#print 'first 5 words'
print json.dumps(words[0:5], indent=1)


#find and print the most common words in the tweets, in the screen_names and in the hashtags
for item in [words, screen_names, hashtags]:
	c = Counter(item)
	print c.most_common()[:10] #top 10
	print


#take the contents and throw it in a pretty table to output

for label, data in (('Word', words),
					('Screen Name', screen_names),
					('Hashtag', hashtags)):
	pt = PrettyTable(field_names=[label, 'Count'])
	c = Counter(data)
	[ pt.add_row(kv) for kv in c.most_common()[:100]]
	pt.align[label], pt.align['Count'] = 'l', 'r'
	print pt


# Calculate lexical diversity of tweets
def lexical_diversity(tokens):
	return 1.0*len(set(tokens))/len(tokens)

def average_words(statuses):
	total_words = sum([ len(s.split()) for s in statuses])
	return 1.0*total_words/len(statuses)

# explnation on page 34
#print 'Words'
#print lexical_diversity(words)
#print 'Screen Names'
#print lexical_diversity(screen_names)
#print 'Hash Tags'
#print lexical_diversity(hashtags)
#print 'Status Text'
#rint lexical_diversity(status_texts)


retweets = [
	(status['retweet_count'],
	 status['retweeted_status']['user']['screen_name'],
	 status['text'])

		for status in statuses 
		if status.has_key('retweeted_status')
	]

pt2 = PrettyTable(field_names=['Count', 'Screen Name', 'Text'])
[pt2.add_row(row) for row in sorted(retweets, reverse=True)[:5] ]
pt2.max_width['Text'] = 50
pt2.align = 'l'
print pt2 


#twitter interest graph




