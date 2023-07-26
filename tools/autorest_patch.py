"""
Run after regenerating the autorest content to update generated files with customizations.
"""

create_method = '''
    @staticmethod
    def create(username, password, url):
        """Creates a new instance of EMS API client. This client will automatically manage 
        API tokens for the given username/password.
        
        :param username: The username to use for authentication.
        :type username: str
        :param password: The password to use for authentication.
        :type password: str
        :param url: The EMS API endpoint to connect to. This should include the /api part at the end of the URL.
        :type url: str
        """
        from .extensions import EmsApiTokenAuthentication
        credentials = EmsApiTokenAuthentication(username, password, url)
        client = emsapi(credentials, url)
        credentials.set_config(client.config)
        return client
'''

find_method = '''
    def find_ems_system_id(self, name):
        """Finds the EMS system id for the given name.
        
        :param name: The EMS system name to search for.
        :type name: str
        """
        from .extensions import EmsSystemHelper
        return EmsSystemHelper.find_id(self, name)
'''

is_error_method = '''
    def is_error(self, response):
        """Returns True if the response represents an error"""
        from .extensions import ErrorHelper
        return ErrorHelper.is_error(response)
'''

get_error_message_method = '''
    def get_error_message(self, response):
        """Returns the error message if there was an error in the request, or None otherwise"""
        from .extensions import ErrorHelper
        return ErrorHelper.get_error_message(response)
'''

import os
this_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(this_dir)
client_file = os.path.join(parent_dir, "emsapi", "emsapi.py")

with open(client_file, "a+") as client:
    client.write(create_method)
    client.write(find_method)
    client.write(is_error_method)
    client.write(get_error_message_method)

database_extension_methods = '''
    def create_from_dataframe(self, ems_system_id, database_id, data, columns_key, max_insert=500, custom_headers=None, raw=False, **operation_config):
        """Creates data entities in the database from a DataFrame. A key
         value pair of column names to EMS Field ID must be passed for this
          to work.
        :param ems_system_id: The unique identifier of the system containing
         the EMS data.
        :type ems_system_id: int
        :param database_id: The unique identifier of the EMS database to add
         data entities to.
        :type database_id: str
        :param data: The entries to be created
        :type data: pandas DataFrame
        :param columns_key: A lookup dictionaty used to match the data
         column names to the corresponding EMS Field ID. The keys need to
         match the data column name and the values need to match the EMS
         field IDs
        :type columns_key: dict
        :param max_insert: the maximum number of rows to insert with each
         create call. This is used to limit the cahnces of a call timeout
        :type max_insert: int
        :return: None
        :rtype: None
        """
        counter = 0
        while counter < len(data):
            body = self._generate_create_body(data, columns_key)
            self.run_create(ems_system_id, database_id, body, custom_headers, raw, operation_config)
            counter += max_insert


    def _generate_create_body(self, data, columns_key):
        """Generates the json body to insert data entities in the database
         from a DataFrame. A key value pair of column names to EMS Field IDs
          must be passed for this to work.
        :param data: The entries to be created
        :type data: pandas DataFrame
        :param columns_key: A lookup dictionaty used to match the data
         column names to the corresponding EMS Field ID. The keys need to
         match the data column name and the values need to match the EMS
         field IDs
        :type columns_key: dict
        :return: json of the body to be used for the create call.
        :rtype: dict
        """
        import pandas as pd
        body = body = {"createColumns": []}
        for i, row in data.iterrows():
            body_chunk = []
            for key,value in row.items():
                # If the value is NaN or '', we can skip adding. The DB will set these to Null
                if (pd.isnull(value)) and (not value == ''):
                    body_chunck_row = {}
                    body_chunck_row['fieldId'] = columns_key[key]
                    body_chunck_row['value'] = value
                    body_chunk.append(body_chunck_row)
            body['createColumns'].append(body_chunk)
        return body
'''

database_file = os.path.join(parent_dir, "emsapi", "operations", "database_operations.py")
with open(database_file, "a+") as database:
    database.write(database_extension_methods)