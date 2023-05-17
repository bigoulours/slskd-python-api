from .base import *

class OptionsApi(BaseApi):
    """
    This class contains the methods to interact with the Options API.
    """

    def get(self) -> dict:
        """
        Gets the current application options.
        """
        url = self.api_url + '/options'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def get_startup(self) -> dict:
        """
        Gets the application options provided at startup.
        """
        url = self.api_url + '/options/startup'
        response = requests.get(url, headers=self.header)
        return response.json()

  
# Getting error 'Unauthorized':
    # def get_debug(self) -> dict:
    #     """
    #     Gets the debug view of the current application options.
    #     """
    #     url = self.api_url + '/options/debug'
    #     response = requests.get(url, headers=self.header)
    #     return response.json()
    