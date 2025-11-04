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

from ._base import *
from ._types import *


class EventsApi(BaseApi):
    """
    This class contains the methods to interact with the Events API.
    """

    def get(self,
            start: int = 0,
            limit: int = 100,
        ) -> list[Event]:
        """
        Retrieves a paginated list of past event records.
        
        :param start: The offset (number of records) at which to start the requested page.
        :param limit: The page size.
        """
        url = self.api_url + '/events'
        response = self.session.get(url)
        return response.json()

    def create(self,
            event_type: EventType,
            data: str = '', # TODO: figure out how this works
        ) -> bool:
        """
        Raises a sample event of the specified type.

        :return: True if successful.
        """
        url = self.api_url + f'/events/{event_type}'
        response = self.session.post(url, json=data)
        return response.ok