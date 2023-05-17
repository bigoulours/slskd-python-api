from .base import *

class PublicChatApi(BaseApi):
    """
    [UNTESTED] This class contains the methods to interact with the PublicChat API.
    """

    def start(self) -> bool:
        """
        Starts public chat.

        :return: True if successful.
        """
        url = self.api_url + '/publicchat'
        response = requests.post(url, headers=self.header)
        return response.ok
    

    def stop(self) -> bool:
        """
        Stops public chat.

        :return: True if successful.
        """
        url = self.api_url + '/publicchat'
        response = requests.delete(url, headers=self.header)
        return response.ok
