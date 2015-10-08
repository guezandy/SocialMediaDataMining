#Which of your connections are the most similar based upon a criterion like job title?

#which of your connections have worked in companies you want to work for?

#where do most of your connections reside geographically?

#Making Linkedin api requests
#https://www.linkedin.com/secure/developer
#create an application
#on terminal: pip install python-linkedin

from linkedin import linkedin 

# Define CONSUMER_KEY, CONSUMER_SECRET,  
# USER_TOKEN, and USER_SECRET from the credentials 
# provided in your LinkedIn application

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
USER_TOKEN = ''
USER_SECRET = ''

RETURN_URL = '' # Not required for developer authentication

# Instantiate the developer authentication class

auth = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                USER_TOKEN, USER_SECRET, 
                                RETURN_URL, 
                                permissions=linkedin.PERMISSIONS.enums.values())

# Pass it in to the app...

app = linkedin.LinkedInApplication(auth)

# Use the app...

app.get_profile()