from .base import *

class SessionApi(BaseApi):

    def auth_valid(self):
        """
        Checks whether the provided authentication is valid.
        """
        url = self.api_url + '/session'
        response = requests.get(url, headers=self.header)
        return response.ok
    

    def login(self, username, password):
        """
        Logs in.
        """
        url = self.api_url + '/session'
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(url, headers=self.header, json=data)
        return response.json()
    

    def security_enabled(self):
        """
        Checks whether security is enabled.
        """
        url = self.api_url + '/session/enabled'
        response = requests.get(url, headers=self.header)
        return response.json()