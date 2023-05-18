from .base import *
from typing import Union

class TransfersApi(BaseApi):
    """
    This class contains the methods to interact with the Transfers API.
    """

    def cancel_download(self, username: str, id:str, remove: bool = False) -> bool:
        """
        Cancels the specified download.

        :return: True if successful.
        """
        url = self.api_url + f'/transfers/downloads/{username}/{id}'
        params = dict(
            remove=remove
        )
        response = requests.delete(url, headers=self.header, params=params)
        return response.ok
    

    def get_download(self, username: str, id: str) -> dict:
        """
        Gets the specified download.
        """
        url = self.api_url + f'/transfers/downloads/{username}/{id}'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def remove_completed_downloads(self) -> bool:
        """
        Removes all completed downloads, regardless of whether they failed or succeeded.

        :return: True if successful.
        """
        url = self.api_url + '/transfers/downloads/all/completed'
        response = requests.delete(url, headers=self.header)
        return response.ok
    

    def cancel_upload(self, username: str, id: str, remove: bool = False) -> bool:
        """
        Cancels the specified upload.

        :return: True if successful.
        """
        url = self.api_url + f'/transfers/uploads/{username}/{id}'
        params = dict(
            remove=remove
        )
        response = requests.delete(url, headers=self.header, params=params)
        return response.ok
    

    def get_upload(self, username: str, id: str) -> dict:
        """
        Gets the specified upload.
        """
        url = self.api_url + f'/transfers/uploads/{username}/{id}'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def remove_completed_uploads(self) -> bool:
        """
        Removes all completed uploads, regardless of whether they failed or succeeded.

        :return: True if successful.
        """
        url = self.api_url + '/transfers/uploads/all/completed'
        response = requests.delete(url, headers=self.header)
        return response.ok
    

    def enqueue(self, username: str, files: list) -> bool:
        """
        Enqueues the specified download.

        :param username: User to download from.
        :param files: A list of dictionaries in the same form as what's returned 
            by :py:func:`~slskd_api.apis.SearchesApi.search_responses`:
            [{'filename': <filename>, 'size': <filesize>}...]
        :return: True if successful.
        """
        url = self.api_url + f'/transfers/downloads/{username}'
        response = requests.post(url, headers=self.header, json=files)
        return response.ok
    

    def get_downloads(self, username: str) -> dict:
        """
        Gets all downloads for the specified username.
        """
        url = self.api_url + f'/transfers/downloads/{username}'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def get_all_downloads(self, includeRemoved: bool = False) -> list:
        """
        Gets all downloads.
        """
        url = self.api_url + '/transfers/downloads/'
        params = dict(
            includeRemoved=includeRemoved
        )
        response = requests.get(url, headers=self.header, params=params)
        return response.json()
    

    def get_queue_position(self, username: str, id: str) -> Union[int,str]:
        """
        Gets the download for the specified username matching the specified filename, and requests the current place in the remote queue of the specified download.
        
        :return: Queue position or error message
        """
        url = self.api_url + f'/transfers/downloads/{username}/{id}/position'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def get_all_uploads(self, includeRemoved: bool = False) -> list:
        """
        Gets all uploads.
        """
        url = self.api_url + '/transfers/uploads/'
        params = dict(
            includeRemoved=includeRemoved
        )
        response = requests.get(url, headers=self.header, params=params)
        return response.json()
    

    def get_uploads(self, username: str) -> dict:
        """
        Gets all uploads for the specified username.
        """
        url = self.api_url + f'/transfers/uploads/{username}'
        response = requests.get(url, headers=self.header)
        return response.json()