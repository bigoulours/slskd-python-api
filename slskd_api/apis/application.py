from .base import *

class ApplicationApi(BaseApi):
    """
    This class contains the methods to interact with the Application API.
    """

    def state(self) -> dict:
        """
        Gets the current state of the application.
        """
        url = self.api_url + '/application'
        response = requests.get(url, headers=self.header)
        return response.json()
    

# Getting Error 'Unauthorized' even with admin API-Key:
    # def stop(self):
    #     """
    #     Stops the application.
    #     """
    #     url = self.api_url + '/application'
    #     response = requests.delete(url, headers=self.header)
    #     return response.ok
    

# Getting Error 'Unauthorized' even with admin API-Key:
    # def restart(self):
    #     """
    #     Restarts the application.
    #     """
    #     url = self.api_url + '/application'
    #     response = requests.put(url, headers=self.header)
    #     return response.json()
    

    def version(self) -> str:
        """
        Gets the current application version.
        """
        url = self.api_url + '/application/version'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def check_updates(self, forceCheck: bool = False) -> dict:
        """
        Checks for updates.
        """
        url = self.api_url + '/application/version/latest'
        params = dict(
            forceCheck=forceCheck
        )
        response = requests.get(url, headers=self.header, params=params)
        return response.json()
    

    def gc(self) -> bool:
        """
        Forces garbage collection.

        :return: True if successful.
        """
        url = self.api_url + '/application/gc'
        response = requests.post(url, headers=self.header)
        return response.ok
    
    
# Getting error 'Could not find file...':
    # def dump(self):
    #     """
    #     """
    #     url = self.api_url + '/application/dump'
    #     response = requests.get(url, headers=self.header)
    #     return response.json()