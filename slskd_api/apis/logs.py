from .base import *

class LogsApi(BaseApi):
    """
    This class contains the methods to interact with the Logs API.
    """

    def get(self) -> list:
        """
        Gets the last few application logs.
        """
        url = self.api_url + '/logs'
        response = requests.get(url, headers=self.header)
        return response.json()