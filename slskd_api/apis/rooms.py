from .base import *

class RoomsApi(BaseApi):

    def get_joined(self):
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


    # ToDo: add missing rooms methods


    def get_all(self):
        """
        Gets a list of rooms from the server.
        """
        url = self.api_url + '/rooms/available'
        response = requests.get(url, headers=self.header)
        return response.json()