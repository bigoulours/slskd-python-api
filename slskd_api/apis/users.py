# Copyright (C) 2023 bigoulours
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .base import *

class UsersApi(BaseApi):
    """
    This class contains the methods to interact with the Users API.
    """

    def address(self, username: str) -> dict:
        """
        Retrieves the address of the specified username.
        """
        url = self.api_url + f'/users/{username}/endpoint'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def browse(self, username: str) -> dict:
        """
        Retrieves the files shared by the specified username.
        """
        url = self.api_url + f'/users/{username}/browse'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def browsing_status(self, username: str):
        """
        Retrieves the status of the current browse operation for the specified username, if any.
        Will return error 404 if called after the browsing operation has ended.
        Best called asynchronously while :py:func:`browse` is still running.
        """
        url = self.api_url + f'/users/{username}/browse/status'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def directory(self, username: str, directory: str) -> dict:
        """
        Retrieves the files from the specified directory from the specified username.
        """
        url = self.api_url + f'/users/{username}/directory'
        data = {
            "directory": directory
        }
        response = requests.post(url, headers=self.header, json=data)
        return response.json()
    

    def info(self, username: str) -> dict:
        """
        Retrieves information about the specified username.
        """
        url = self.api_url + f'/users/{username}/info'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def status(self, username: str) -> dict:
        """
        Retrieves status for the specified username.
        """
        url = self.api_url + f'/users/{username}/status'
        response = requests.get(url, headers=self.header)
        return response.json()