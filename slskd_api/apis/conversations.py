from .base import *

class ConversationsApi(BaseApi):
    """
    This class contains the methods to interact with the Conversations API.
    """

    def acknowledge(self, username, id):
        """
        Acknowledges the given message id for the given username.
        """
        url = self.api_url + f'/conversations/{username}/{id}'
        response = requests.put(url, headers=self.header)
        return response.json()
    

    def acknowledge_all(self, username):
        """
        Acknowledges all messages from the given username.
        """
        url = self.api_url + f'/conversations/{username}'
        response = requests.put(url, headers=self.header)
        return response.json()
    

    def delete(self, username):
        """
        Closes the conversation associated with the given username.
        """
        url = self.api_url + f'/conversations/{username}'
        response = requests.delete(url, headers=self.header)
        return response.json()
    

    def get(self, username, includeMessages=True):
        """
        Gets the conversation associated with the specified username.
        """
        url = self.api_url + f'/conversations/{username}'
        params = dict(
            includeMessages=includeMessages
        )
        response = requests.get(url, headers=self.header, params=params)
        return response.json()
    

    def send(self, username, message):
        """
        Sends a private message to the specified username.
        """
        url = self.api_url + f'/conversations/{username}'
        response = requests.post(url, headers=self.header, json=message)
        return response
    

    def get_all(self, includeInactive=False, unAcknowledgedOnly=False):
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
    

    def get_messages(self, username, unAcknowledgedOnly=False):
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
    