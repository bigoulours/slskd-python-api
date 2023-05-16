from .base import *

class RoomsApi(BaseApi):
    """
    This class contains the methods to interact with the Rooms API.
    """

    def get_all_joined(self):
        """
        Gets all joined rooms.
        """
        url = self.api_url + '/rooms/joined'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def join(self, room):
        """
        Joins a room.
        """
        url = self.api_url + '/rooms/joined'
        response = requests.post(url, headers=self.header, json=room)
        return response.json()


    def get_joined(self, roomName):
        """
        Gets the specified room.
        """
        url = self.api_url + f'/rooms/joined/{roomName}'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def leave(self, roomName):
        """
        Leaves a room.
        """
        url = self.api_url + f'/rooms/joined/{roomName}'
        response = requests.delete(url, headers=self.header)
        return response.ok
    

    def send(self, roomName, message):
        """
        Sends a message to the specified room.
        """
        url = self.api_url + f'/rooms/joined/{roomName}/messages'
        response = requests.post(url, headers=self.header, json=message)
        return response.ok


    def get_messages(self, roomName):
        """
        Gets the current list of messages for the specified room.
        """
        url = self.api_url + f'/rooms/joined/{roomName}/messages'
        response = requests.get(url, headers=self.header)
        return response.json()


    def set_tocker(self, roomName, ticker):
        """
        Sets a ticker for the specified room.
        """
        url = self.api_url + f'/rooms/joined/{roomName}/ticker'
        response = requests.post(url, headers=self.header, json=ticker)
        return response.ok
    

    def add_member(self, roomName, username):
        """
        Adds a member to a private room.
        """
        url = self.api_url + f'/rooms/joined/{roomName}/members'
        response = requests.post(url, headers=self.header, json=username)
        return response.ok
    

    def get_users(self, roomName):
        """
        Gets the current list of users for the specified room.
        """
        url = self.api_url + f'/rooms/joined/{roomName}/users'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def get_all(self):
        """
        Gets a list of rooms from the server.
        """
        url = self.api_url + '/rooms/available'
        response = requests.get(url, headers=self.header)
        return response.json()