import getpass
import json
import msrest
import pandas
import requests
import sys

from emsapi import emsapi
from msrest import authentication

url = "https://ems.efoqa.com/api/"
user = input('Enter your EFOQA username: ')
pwd = getpass.getpass(prompt = 'Enter your EFOQA password: ')

# Authenticate with EMS API
authorizationUrl = url + "token"
body = "grant_type=password&username=" + user +"&password=" + pwd
authorizationResponse = requests.post(authorizationUrl, body)

# Describe the results of the test
if authorizationResponse.ok:
    print("Successfully authenticated with the EMS API and retrieved a bearer token.")
else:
    print("Unable to authenticate with the EMS API.")
    
# Set up the autorest session with the basic authentication type using bearer token.

session = authentication.BasicTokenAuthentication(json.loads(authorizationResponse.text))
client = emsapi(session, url)

# Print the systems the user has access to in order to demonstrate the API.
systems = client.ems_system.get_ems_systems()

# Create a list out of the systems list that contains only the information we want.
sysList = list(map(lambda system: [system.id, system.name, system.description], systems))
df = pandas.DataFrame(sysList, columns=['id', 'name', 'description'])

print("You have access to the following systems:")
print(df.head())