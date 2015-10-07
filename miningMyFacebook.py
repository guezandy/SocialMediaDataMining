import facebook
import json

#method for pretty printing
ACCESS_TOKEN = 'CAACEdEose0cBAMwOOR8EWW4UdjEDABmv4NMcLK0bDCguQ9P7xAFeOZAquMZAtTScxkOG0o630YSEuPQGbjTjL7emdfRoYp6ZC1YYKqErvwzlg7QFrzVjIMUhLvmuKZB0uA4CZBjaZC9H5Bi97FeZAooZCPHqZCZBjSo9r2vxifgAiz0LI4Lk9DOJ7F98Lz5W4syTeMcKxaZCMLDBvUCNhk9BTZC9'

def pp(o):
	print json.dumps(0, indent=1)

g = facebook.GraphAPI(ACCESS_TOKEN)
print g
print '---------------'
print 'Me'
print '---------------'
pp(g.get_object('me'))
print
print '---------------'
print 'My Friends'
print '---------------'
pp(g.get_connections('me', 'friends'))
print
print '---------------'
print 'Social Web'
print '---------------'
pp(g.request("search", {'q' : 'social web', 'type' : 'page'}))

