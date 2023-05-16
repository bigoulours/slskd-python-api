from .base import *

class TransfersApi(BaseApi):
    """
    This class contains the methods to interact with the Transfers API.
    """

    def cancel_download(self, username, id, remove=False):
        """
        Cancels the specified download.
        """
        url = self.api_url + f'/transfers/downloads/{username}/{id}'
        params = dict(
            remove=remove
        )
        response = requests.delete(url, headers=self.header, params=params)
        return response.ok
    

    def get_download(self, username, id):
        """
        Gets the specified download.
        """
        url = self.api_url + f'/transfers/downloads/{username}/{id}'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def remove_completed_downloads(self):
        """
        Removes all completed downloads, regardless of whether they failed or succeeded.
        """
        url = self.api_url + '/transfers/downloads/all/completed'
        response = requests.delete(url, headers=self.header)
        return response.ok
    

    def cancel_upload(self, username, id, remove=False):
        """
        Cancels the specified upload.
        """
        url = self.api_url + f'/transfers/uploads/{username}/{id}'
        params = dict(
            remove=remove
        )
        response = requests.delete(url, headers=self.header, params=params)
        return response.ok
    

    def get_upload(self, username, id):
        """
        Gets the specified upload.
        """
        url = self.api_url + f'/transfers/uploads/{username}/{id}'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def remove_completed_uploads(self):
        """
        Removes all completed uploads, regardless of whether they failed or succeeded.
        """
        url = self.api_url + '/transfers/uploads/all/completed'
        response = requests.delete(url, headers=self.header)
        return response.ok
    

    def enqueue(self, username, files):
        """
        Enqueues the specified download.
        """
        url = self.api_url + f'/transfers/downloads/{username}'
        response = requests.post(url, headers=self.header, json=files)
        return response.json()
    

    def get_downloads(self, username):
        """
        Gets all downloads for the specified username.
        """
        url = self.api_url + f'/transfers/downloads/{username}'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def get_all_downloads(self, includeRemoved=False):
        """
        Gets all downloads.
        """
        url = self.api_url + '/transfers/downloads/'
        params = dict(
            includeRemoved=includeRemoved
        )
        response = requests.get(url, headers=self.header, params=params)
        return response.json()
    

    def get_queue_position(self, username, id):
        """
        Gets the download for the specified username matching the specified filename, and requests the current place in the remote queue of the specified download.
        """
        url = self.api_url + f'/transfers/downloads/{username}/{id}/position'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def get_all_uploads(self, includeRemoved=False):
        """
        Gets all uploads.
        """
        url = self.api_url + '/transfers/uploads/'
        params = dict(
            includeRemoved=includeRemoved
        )
        response = requests.get(url, headers=self.header, params=params)
        return response.json()
    

    def get_uploads(self, username):
        """
        Gets all uploads for the specified username.
        """
        url = self.api_url + f'/transfers/uploads/{username}'
        response = requests.get(url, headers=self.header)
        return response.json()