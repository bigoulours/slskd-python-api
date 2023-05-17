from .base import *

class RelayApi(BaseApi):
    """
    [UNTESTED] This class contains the methods to interact with the Relay API.
    """

    def connect(self):
        """
        Connects to the configured controller.
        """
        url = self.api_url + '/relay/agent'
        response = requests.put(url, headers=self.header)
        return response.ok
    

    def disconnect(self):
        """
        Disconnects from the connected controller.
        """
        url = self.api_url + '/relay/agent'
        response = requests.delete(url, headers=self.header)
        return response.ok
    

    def download_file(self, token):
        """
        Downloads a file from the connected controller.
        """
        url = self.api_url + f'/relay/controller/downloads/{token}'
        response = requests.get(url, headers=self.header)
        return response.ok
    

    def upload_file(self, token):
        """
        Uploads a file from the connected controller.
        """
        url = self.api_url + f'/relay/controller/files/{token}'
        response = requests.post(url, headers=self.header)
        return response.ok
    

    def upload_share_info(self, token):
        """
        Uploads share information to the connected controller.
        """
        url = self.api_url + f'/relay/controller/shares/{token}'
        response = requests.post(url, headers=self.header)
        return response.ok