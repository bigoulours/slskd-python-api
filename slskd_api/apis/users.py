from .base import *

class UsersApi(BaseApi):
    """
    This class contains the methods to interact with the Users API.
    """

    def address(self, username: str) -> dict:
        """
        Retrieves the address of the specified username.
        """
        url = self.api_url + f'/users/{username}/endpoint'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def browse(self, username: str) -> dict:
        """
        Retrieves the files shared by the specified username.
        """
        url = self.api_url + f'/users/{username}/browse'
        response = requests.get(url, headers=self.header)
        return response.json()
    

# Getting Error 404 'Not Found' 
    # def browsing_status(self, username: str):
    #     """
    #     Retrieves the status of the current browse operation for the specified username, if any.
    #     """
    #     url = self.api_url + f'/users/{username}/browse/status'
    #     response = requests.get(url, headers=self.header)
    #     return response.json()
    

    def directory(self, username: str, directory: str) -> dict:
        """
        Retrieves the files from the specified directory from the specified username.
        """
        url = self.api_url + f'/users/{username}/directory'
        data = {
            "directory": directory
        }
        response = requests.post(url, headers=self.header, json=data)
        return response.json()
    

    def info(self, username: str) -> dict:
        """
        Retrieves information about the specified username.
        """
        url = self.api_url + f'/users/{username}/info'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def status(self, username: str) -> dict:
        """
        Retrieves status for the specified username.
        """
        url = self.api_url + f'/users/{username}/status'
        response = requests.get(url, headers=self.header)
        return response.json()