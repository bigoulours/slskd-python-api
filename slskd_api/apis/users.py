from .base import *

class UsersApi(BaseApi):

    def endpoint(self, username):
        """
        Retrieves the address of the specified username.
        """
        url = self.api_url + f'/users/{username}/endpoint'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def browse(self, username):
        """
        Retrieves the files shared by the specified username.
        """
        url = self.api_url + f'/users/{username}/browse'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def browsing_status(self, username):
        """
        Retrieves the status of the current browse operation for the specified username, if any.
        """
        url = self.api_url + f'/users/{username}/browse/status'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def directory(self, username, directory):
        """
        Retrieves the files from the specified directory from the specified username.
        """
        url = self.api_url + f'/users/{username}/directory'
        response = requests.post(url, headers=self.header, json=directory)
        return response.json()
    

    def info(self, username):
        """
        Retrieves information about the specified username.
        """
        url = self.api_url + f'/users/{username}/info'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def status(self, username):
        """
        Retrieves status for the specified username.
        """
        url = self.api_url + f'/users/{username}/status'
        response = requests.get(url, headers=self.header)
        return response.json()