from .base import *

class SharesApi(BaseApi):
    """
    This class contains the methods to interact with the Shares API.
    """

    def get_all(self) -> dict:
        """
        Gets the current list of shares.
        """
        url = self.api_url + '/shares'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def start_scan(self) -> bool:
        """
        Initiates a scan of the configured shares.

        :return: True if successful.
        """
        url = self.api_url + '/shares'
        response = requests.put(url, headers=self.header)
        return response.ok
    

    def cancel_scan(self) -> bool:
        """
        Cancels a share scan, if one is running.

        :return: True if successful.
        """
        url = self.api_url + '/shares'
        response = requests.delete(url, headers=self.header)
        return response.ok
    

    def get(self, id: str) -> dict:
        """
        Gets the share associated with the specified id.
        """
        url = self.api_url + f'/shares/{id}'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def all_contents(self) -> list:
        """
        Returns a list of all shared directories and files.
        """
        url = self.api_url + '/shares/contents'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def contents(self, id: str) -> list:
        """
        Gets the contents of the share associated with the specified id.
        """
        url = self.api_url + f'/shares/{id}/contents'
        response = requests.get(url, headers=self.header)
        return response.json()