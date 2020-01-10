"""
Run after regenerating the autorest content to update generated files with customizations.
"""

create_method = '''

    @staticmethod
    def create(username, password, url='https://ems.efoqa.com/api'):
        """Creates a new instance of EMS API client. This client will automatically manage 
        API tokens for the given username/password.
        
        :param username: The username to use for authentication.
        :type username: str
        :param password: The password to use for authentication.
        :type password: str
        :param url: The EMS API endpoint to connect to (default: {'https://ems.efoqa.com/api'})
        :type url: str
        """
        from .auth import EmsApiTokenAuthentication
        session = EmsApiTokenAuthentication(username, password, url)
        return emsapi(session, url)
'''

import os
this_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(this_dir)
client_file = os.path.join(parent_dir, "emsapi", "emsapi.py")

with open(client_file, "a+") as client:
    client.write(create_method)