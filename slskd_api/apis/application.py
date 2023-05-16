from .base import *

class ApplicationApi(BaseApi):
    """
    This class contains the methods to interact with the Application API.
    """

    def state(self):
        """
        Gets the current state of the application.
        """
        url = self.api_url + '/application'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def stop(self):
        """
        Stops the application.
        """
        url = self.api_url + '/application'
        response = requests.delete(url, headers=self.header)
        return response.json()
    

    def restart(self):
        """
        Restarts the application.
        """
        url = self.api_url + '/application'
        response = requests.put(url, headers=self.header)
        return response.json()
    

    def version(self):
        """
        Gets the current application version.
        """
        url = self.api_url + '/application/version'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def check_updates(self, forceCheck=False):
        """
        Checks for updates.
        """
        url = self.api_url + '/application/version/latest'
        params = dict(
            forceCheck=forceCheck
        )
        response = requests.get(url, headers=self.header, params=params)
        return response.json()
    

    def gc(self):
        """
        Forces garbage collection.
        """
        url = self.api_url + '/application/gc'
        response = requests.post(url, headers=self.header)
        return response.json()
    
    
    # def application_dump(self):
    #     """
    #     Returns error 'Could not find file...'
    #     """
    #     url = self.api_url + '/application/dump'
    #     response = requests.get(url, headers=self.header)
    #     return response.json()