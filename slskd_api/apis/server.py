from .base import *

class ServerApi(BaseApi):
    """
    This class contains the methods to interact with the Search API.
    """

    def connect(self) -> bool:
        """
        Connects the client.

        :return: True if successful.
        """
        url = self.api_url + '/server'
        response = requests.put(url, headers=self.header)
        return response.ok
    

    def disconnect(self) -> bool:
        """
        Disconnects the client.

        :return: True if successful.
        """
        url = self.api_url + '/server'
        response = requests.delete(url, headers=self.header, json='')
        return response.ok
    

    def state(self) -> dict:
        """
        Retrieves the current state of the server.
        """
        url = self.api_url + '/server'
        response = requests.get(url, headers=self.header)
        return response.json()