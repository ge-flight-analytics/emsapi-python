import getpass
import json
import pandas
import requests
import sys

from emsapi import emsapi

url = "https://ems.efoqa.com/api/"
user = input('Enter your EFOQA username: ')
pwd = getpass.getpass(prompt = 'Enter your EFOQA password: ')

client = emsapi.create(user, pwd, url)

# Print the systems the user has access to in order to demonstrate the API.
systems = client.ems_system.get_ems_systems()
sysList = list(map(lambda system: [system.id, system.name, system.description], systems))
df = pandas.DataFrame(sysList, columns=['id', 'name', 'description'])

print("You have access to the following systems:")
print(df.head())

# Print the offsets for a parameter of a flight.

# Baro-corrected altitude
altitudeId = "H4sIAAAAAAAEAG2Q0QuCMBDG34P+B/HdbZVUiApBPQT2kgi9rrn0YM7aZvbnN5JVUvdwfHD34/vu4iPXrbjTs+D7kksDF+DKezRC6ggSvzbmGmHc9z3qF6hVFZ4TMsOnQ5azmjc0AKkNlYz7A/Mm9GusUUkNZa00ijLj+BCTFd6UgApF/XQ68bx4SMHVvkyd1GjX6KytgFER46+FEZBfObOZ2db6eBBJEIlvVGfz4P+LhYRbZ29NyVCzgJD1MgitDIhrrj6+P/h04obj36VPLpuOeVIBAAA="

# EMS7 - the demo system.
emsId = client.find_ems_system_id('ems7-app')

# A flight that is known to exist
flightId = 190

# Pull out altitude with 100 samples through the file.
query = {
    "select": [
        {
            "analyticId": altitudeId
        }
    ],
    "size": 100
}

# Execute the API call.
altitude = client.analytic.get_query_results(emsId, flightId, query)
print(altitude.offsets)