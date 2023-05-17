from .base import *

class RoomsApi(BaseApi):
    """
    This class contains the methods to interact with the Rooms API.
    """

    def get_all_joined(self) -> list:
        """
        Gets all joined rooms.

        :return: Names of the joined rooms.
        """
        url = self.api_url + '/rooms/joined'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def join(self, roomName: str) -> dict:
        """
        Joins a room.

        :return: room info: name, isPrivate, users, messages
        """
        url = self.api_url + '/rooms/joined'
        response = requests.post(url, headers=self.header, json=roomName)
        return response.json()


    def get_joined(self, roomName: str) -> dict:
        """
        Gets the specified room.

        :return: room info: name, isPrivate, users, messages
        """
        url = self.api_url + f'/rooms/joined/{roomName}'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def leave(self, roomName: str) -> bool:
        """
        Leaves a room.

        :return: True if successful.
        """
        url = self.api_url + f'/rooms/joined/{roomName}'
        response = requests.delete(url, headers=self.header)
        return response.ok
    

    def send(self, roomName: str, message: str) -> bool:
        """
        Sends a message to the specified room.

        :return: True if successful.
        """
        url = self.api_url + f'/rooms/joined/{roomName}/messages'
        response = requests.post(url, headers=self.header, json=message)
        return response.ok


    def get_messages(self, roomName: str) -> list:
        """
        Gets the current list of messages for the specified room.
        """
        url = self.api_url + f'/rooms/joined/{roomName}/messages'
        response = requests.get(url, headers=self.header)
        return response.json()


    def set_ticker(self, roomName: str, ticker: str) -> bool:
        """
        Sets a ticker for the specified room.

        :return: True if successful.
        """
        url = self.api_url + f'/rooms/joined/{roomName}/ticker'
        response = requests.post(url, headers=self.header, json=ticker)
        return response.ok
    

    def add_member(self, roomName: str, username: str) -> bool:
        """
        Adds a member to a private room.

        :return: True if successful.
        """
        url = self.api_url + f'/rooms/joined/{roomName}/members'
        response = requests.post(url, headers=self.header, json=username)
        return response.ok
    

    def get_users(self, roomName: str) -> list:
        """
        Gets the current list of users for the specified joined room.
        """
        url = self.api_url + f'/rooms/joined/{roomName}/users'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def get_all(self) -> list:
        """
        Gets a list of rooms from the server.
        """
        url = self.api_url + '/rooms/available'
        response = requests.get(url, headers=self.header)
        return response.json()