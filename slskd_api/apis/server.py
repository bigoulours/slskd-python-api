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
from typing import TypedDict, Literal

class ServerState(TypedDict):
    """
    TypedDict describing server state. Returned by :py:meth:`~slskd_api.apis.ServerApi.state`.
    """
    address: str
    ipEndPoint: str
    state: Literal["Connected, LoggedIn", "Disconnected"] # TODO: not sure if complete, but haven't figured out others.
    isConnected: bool
    isLoggedIn: bool
    isTransitioning: bool


class ServerApi(BaseApi):
    """
    This class contains the methods to interact with the Server API.
    """

    def connect(self) -> bool:
        """
        Connects the client.

        :return: True if successful.
        """
        url = self.api_url + '/server'
        response = self.session.put(url)
        return response.ok
    

    def disconnect(self) -> bool:
        """
        Disconnects the client.

        :return: True if successful.
        """
        url = self.api_url + '/server'
        response = self.session.delete(url, json='')
        return response.ok
    

    def state(self) -> ServerState:
        """
        Retrieves the current state of the server.
        """
        url = self.api_url + '/server'
        response = self.session.get(url)
        return response.json()