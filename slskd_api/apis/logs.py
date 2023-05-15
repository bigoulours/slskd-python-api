from .base import *

class LogsApi(BaseApi):

    def get(self):
        """
        Gets the last few application logs.
        """
        url = self.api_url + '/logs'
        response = requests.get(url, headers=self.header)
        return response.json()