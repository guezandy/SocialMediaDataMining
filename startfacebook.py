#Start with Graph API Explorer

#DEMO: start with opening facebook graph api explorer
# get access token
# me?fields=id,name,friends.fields(likes)


#this code makes an http request basically mirroring what the open graph did
#you can use this url in postman
import requests
import json

base_url = 'https://graph.facebook.com/me'
ACCESS_TOKEN = 'CAACEdEose0cBAMwOOR8EWW4UdjEDABmv4NMcLK0bDCguQ9P7xAFeOZAquMZAtTScxkOG0o630YSEuPQGbjTjL7emdfRoYp6ZC1YYKqErvwzlg7QFrzVjIMUhLvmuKZB0uA4CZBjaZC9H5Bi97FeZAooZCPHqZCZBjSo9r2vxifgAiz0LI4Lk9DOJ7F98Lz5W4syTeMcKxaZCMLDBvUCNhk9BTZC9'
#get 10 likes for 10 friends

fields = 'id,name,friends.limit(10).fields(likes.limit(10))'
url = '%s?fields=%s&access_token=%s' % \
	(base_url, fields, ACCESS_TOKEN,)

user_id = '993071184046388'

url = '%s/photos?limit=1&access_token=%s' % \
	(base_url, ACCESS_TOKEN,)

print url 
#put the url into postman to observe the actions

#get the content
content = requests.get(url).json()

#pretty print
print json.dumps(content, indent=1)

#understanding the OpenGraph & facebook's pull on the world
#The rock: http://www.imdb.com/title/tt0117500/
#view source: view-source:http://www.imdb.com/title/tt0117500/
# ctrl + f : og to see the meta tags

#THE ABILITY TO INTERACT WITH OBJECTS
#http://ogp.me/ official ogp documentation
#https://developers.facebook.com/tools/debug/ to see what fb sees



