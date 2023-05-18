from .base import *

class SessionApi(BaseApi):
    """
    This class contains the methods to interact with the Server API.
    """

    def auth_valid(self) -> bool:
        """
        Checks whether the provided authentication is valid.
        """
        url = self.api_url + '/session'
        response = requests.get(url, headers=self.header)
        return response.ok
    

    def login(self, username: str, password: str) -> dict:
        """
        Logs in.

        :return: Session info for the given user incl. token.
        """
        url = self.api_url + '/session'
        data = {
            'username': username,
            'password': password
        }
        response = requests.post(url, headers=self.header, json=data)
        return response.json()
    

    def security_enabled(self) -> bool:
        """
        Checks whether security is enabled.
        """
        url = self.api_url + '/session/enabled'
        response = requests.get(url, headers=self.header)
        return response.json()