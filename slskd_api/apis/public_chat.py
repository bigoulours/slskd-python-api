from .base import *

class PublicChatApi(BaseApi):
    """
    [UNTESTED] This class contains the methods to interact with the PublicChat API.
    """

    def start(self):
        """
        Starts public chat.
        """
        url = self.api_url + '/publicchat'
        response = requests.post(url, headers=self.header)
        return response.ok
    

    def stop(self):
        """
        Stops public chat.
        """
        url = self.api_url + '/publicchat'
        response = requests.delete(url, headers=self.header)
        return response.ok
