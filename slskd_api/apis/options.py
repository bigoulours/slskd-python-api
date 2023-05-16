from .base import *

class OptionsApi(BaseApi):
    """
    This class contains the methods to interact with the Options API.
    """

    def get(self):
        """
        Gets the current application options.
        """
        url = self.api_url + '/options'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def startup(self):
        """
        Gets the application options provided at startup.
        """
        url = self.api_url + '/options/startup'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def debug(self):
        """
        Gets the debug view of the current application options.
        """
        url = self.api_url + '/options/debug'
        response = requests.get(url, headers=self.header)
        return response.json()
    