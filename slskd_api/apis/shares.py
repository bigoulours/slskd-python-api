from .base import *

class SharesApi(BaseApi):
    """
    This class contains the methods to interact with the Shares API.
    """

    def get_all(self):
        """
        Gets the current list of shares.
        """
        url = self.api_url + '/shares'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def start_scan(self):
        """
        Initiates a scan of the configured shares.
        """
        url = self.api_url + '/shares'
        response = requests.put(url, headers=self.header)
        return response
    

    def cancel_scan(self):
        """
        Cancels a share scan, if one is running.
        """
        url = self.api_url + '/shares'
        response = requests.delete(url, headers=self.header)
        return response
    

    def get(self, id):
        """
        Gets the share associated with the specified id.
        """
        url = self.api_url + f'/shares/{id}'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def get_all_contents(self):
        """
        Returns a list of all shared directories and files.
        """
        url = self.api_url + '/shares/contents'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def get_contents(self, id):
        """
        Gets the contents of the share associated with the specified id.
        """
        url = self.api_url + f'/shares/{id}/contents'
        response = requests.get(url, headers=self.header)
        return response.json()