#Which of your connections are the most similar based upon a criterion like job title?

#which of your connections have worked in companies you want to work for?

#where do most of your connections reside geographically?

#Making Linkedin api requests
#https://www.linkedin.com/secure/developer
#create an application
#on terminal: pip install python-linkedin

from linkedin import linkedin
from linkedin import server
import json


# Define CONSUMER_KEY, CONSUMER_SECRET,  
# USER_TOKEN, and USER_SECRET from the credentials 
# provided in your LinkedIn application

KEY = '77llcra3onqkw1'
SECRET = 'ISIgYEfdD3buscg6'
USER_TOKEN = ''
USER_SECRET = ''

RETURN_URL = "http://localhost:8000"
# Optionally one can send custom "state" value that will be returned from OAuth server
# It can be used to track your user state or something else (it's up to you)
# Be aware that this value is sent to OAuth server AS IS - make sure to encode or hash it
#authorization.state = 'your_encoded_message'

	
li = linkedin(KEY, SECRET)
connections = li.connections_api.getMyConnections(access_token)

#authentication = linkedin.LinkedInAuthentication(KEY, SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
#print authentication.authorization_url
#app = linkedin.LinkedInApplication(authentication)
#print app

# Instantiate the developer authentication class
#app = server.quick_api(KEY, SECRET)

# Use the app...

#connections = app.get_connections()
#print connections
#connections_data = 'linkedin_connections.json'

#f = open(connections_data, 'w')
#f.write(json.dumps(connections, indent=1))
#f.close()