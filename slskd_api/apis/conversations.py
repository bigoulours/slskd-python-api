from .base import *

class ConversationsApi(BaseApi):
    """
    This class contains the methods to interact with the Conversations API.
    """

    def acknowledge(self, username: str, id: int) -> bool:
        """
        Acknowledges the given message id for the given username.

        :return: True if successful.
        """
        url = self.api_url + f'/conversations/{username}/{id}'
        response = requests.put(url, headers=self.header)
        return response.ok
    

    def acknowledge_all(self, username: str) -> bool:
        """
        Acknowledges all messages from the given username.

        :return: True if successful.
        """
        url = self.api_url + f'/conversations/{username}'
        response = requests.put(url, headers=self.header)
        return response.ok
    

    def delete(self, username: str) -> bool:
        """
        Closes the conversation associated with the given username.

        :return: True if successful.
        """
        url = self.api_url + f'/conversations/{username}'
        response = requests.delete(url, headers=self.header)
        return response.ok
    

    def get(self, username: str, includeMessages: bool = True) -> dict:
        """
        Gets the conversation associated with the specified username.
        """
        url = self.api_url + f'/conversations/{username}'
        params = dict(
            includeMessages=includeMessages
        )
        response = requests.get(url, headers=self.header, params=params)
        return response.json()
    

    def send(self, username: str, message: str) -> bool:
        """
        Sends a private message to the specified username.

        :return: True if successful.
        """
        url = self.api_url + f'/conversations/{username}'
        response = requests.post(url, headers=self.header, json=message)
        return response.ok
    

    def get_all(self, includeInactive: bool = False, unAcknowledgedOnly : bool = False) -> list:
        """
        Gets all active conversations.
        """
        url = self.api_url + '/conversations'
        params = dict(
            includeInactive=includeInactive,
            unAcknowledgedOnly=unAcknowledgedOnly
        )
        response = requests.get(url, headers=self.header, params=params)
        return response.json()
    

    def get_messages(self, username: str, unAcknowledgedOnly : bool = False) -> list:
        """
        Gets all messages associated with the specified username.
        """
        url = self.api_url + f'/conversations/{username}/messages'
        params = dict(
            username=username,
            unAcknowledgedOnly=unAcknowledgedOnly
        )
        response = requests.get(url, headers=self.header, params=params)
        return response.json()
    