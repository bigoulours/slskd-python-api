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

SortOrderType: TypeAlias = Literal["ASC", "DESC"]

class TelemetryApi(BaseApi):
    """
    This class contains the methods to interact with the Metrics API.
    """

    def get_metrics(self) -> str:
        """
        Gets the Prometheus metrics as text.
        """
        url = self.api_url + '/telemetry/metrics'
        response = self.session.get(url)
        return response.text

    
    def get_kpi(self) -> str:
        """
        Gets application KPIs.
        """
        url = self.api_url + '/telemetry/metrics/kpi'
        response = self.session.get(url)
        return response.text

    
    def get_transfer_summary(self,
                             start: str = None,
                             end: str = None,
                             direction: TransferDirection = None,
                             username: str = None
        ) -> dict:
        """
        Gets a summary of all transfer activity over the specified timeframe, grouped by direction and final state.
        
        :param start: The start time of the window (default: 7 days ago). e.g. "2026-01-31"
        :param end: The end time of the window (default: now). e.g. "2026-02-15"
        """
        params = {
            'start': start,
            'end': end,
            'direction': direction,
            'username': username
        }
        url = self.api_url + '/telemetry/reports/transfers/summary'
        response = self.session.get(url, params=params)
        return response.json()

    
    def get_transfer_histogram(self,
                               start: str = None,
                               end: str = None,
                               interval: int = 60,
                               direction: TransferDirection = None,
                               username: str = None
        ) -> dict:
        """
        Gets a histogram of all transfer activity over the specified timeframe, aggregated into fixed size time intervals and grouped by direction and final state.
        
        :param start: The start time of the window (default: 7 days ago). e.g. "2026-01-31"
        :param end: The end time of the window (default: now). e.g. "2026-02-15"
        :param interval: The interval, in minutes (default: 60).
        """
        params = {
            'start': start,
            'end': end,
            'interval': interval,
            'direction': direction,
            'username': username
        }
        url = self.api_url + '/telemetry/reports/transfers/histogram'
        response = self.session.get(url, params=params)
        return response.json()

    
    def get_transfer_leaderboard(self,
                                 direction: TransferDirection,
                                 start: str = None,
                                 end: str = None,
                                 sortBy: Literal["Count", "TotalBytes", "AverageSpeed"] = 'Count',
                                 sortOrder: SortOrderType = 'DESC',
                                 limit: int = 25,
                                 offset: int = 0
        ) -> list:
        """
        Gets the top N user summaries by count, total bytes, or average speed.
        
        :param start: The start time of the window (default: oldest). e.g. "2026-01-31"
        :param end: The end time of the window (default: now). e.g. "2026-02-15"
        :param sortBy: The property by which to sort.
        :param sortOrder: The sort order.
        :param limit: The number of records to return.
        :param offset: The record offset (if paginating).
        :return: List of users (dict) with transfer related info (count, totalBytes, averageSpeed...)
        """
        params = {
            'direction': direction,
            'start': start,
            'end': end,
            'sortBy': sortBy,
            'sortOrder': sortOrder,
            'limit': limit,
            'offset': offset
        }
        url = self.api_url + '/telemetry/reports/transfers/leaderboard'
        response = self.session.get(url, params=params)
        return response.json()
    
    
    def get_user_transfers(self,
                           username: str,
                           start: str = None,
                           end: str = None
        ) -> dict:
        """
        Gets detailed transfer activity for the specified user.
        
        :param start: The start time of the window (default: oldest). e.g. "2026-01-31"
        :param end: The end time of the window (default: now). e.g. "2026-02-15"
        """
        params = {
            'start': start,
            'end': end
        }
        url = self.api_url + f'/telemetry/reports/transfers/users/{username}'
        response = self.session.get(url, params=params)
        return response.json()


    def get_transfer_exceptions(self,
                                direction: TransferDirection,
                                start: str = None,
                                end: str = None,
                                username: str = None,
                                sortOrder: SortOrderType = 'DESC',
                                limit: int = 25,
                                offset: int = 0
        ) -> list:
        """
        Gets a list of transfer exceptions by direction.
        
        :param start: The start time of the window (default: oldest). e.g. "2026-01-31"
        :param end: The end time of the window (default: now). e.g. "2026-02-15"
        :param username: An optional username by which to filter exceptions.
        :param sortOrder: The sort order.
        :param limit: The number of records to return.
        :param offset: The record offset (if paginating).
        :return: List of exceptions (dict) with transfer related info (direction, filename, state...)
        """
        params = {
            'direction': direction,
            'start': start,
            'end': end,
            'username': username,
            'sortOrder': sortOrder,
            'limit': limit,
            'offset': offset
        }
        url = self.api_url + '/telemetry/reports/transfers/exceptions'
        response = self.session.get(url, params=params)
        return response.json()
    
    
    def get_transfer_exceptions_pareto(self,
                                       direction: TransferDirection,
                                       start: str = None,
                                       end: str = None,
                                       username: str = None,
                                       limit: int = 25,
                                       offset: int = 0
        ) -> list:
        """
        Gets the top N exceptions by total count and direction.
        
        :param start: The start time of the window (default: oldest). e.g. "2026-01-31"
        :param end: The end time of the window (default: now). e.g. "2026-02-15"
        :param username: An optional username by which to filter exceptions.
        :param limit: The number of records to return.
        :param offset: The record offset (if paginating).
        :return: List of exceptions (dict) with following info: exception message, count and distinctUsers.
        """
        params = {
            'direction': direction,
            'start': start,
            'end': end,
            'username': username,
            'limit': limit,
            'offset': offset
        }
        url = self.api_url + '/telemetry/reports/transfers/exceptions/pareto'
        response = self.session.get(url, params=params)
        return response.json()
    
    
    def get_most_dl_directories(self,
                                start: str = None,
                                end: str = None,
                                username: str = None,
                                limit: int = 25,
                                offset: int = 0
        
        ) -> list:
        """
        Gets the top N most frequently downloaded directories by total count and distinct users.
        
        :param start: The start time of the window (default: oldest). e.g. "2026-01-31"
        :param end: The end time of the window (default: now). e.g. "2026-02-15"
        :param username: An optional username by which to filter exceptions.
        :param limit: The number of records to return.
        :param offset: The record offset (if paginating).
        :return: List of directories (dict) with following info: path, count and distinctUsers.
        """
        params = {
            'start': start,
            'end': end,
            'username': username,
            'limit': limit,
            'offset': offset
        }
        url = self.api_url + '/telemetry/reports/transfers/directories'
        response = self.session.get(url, params=params)
        return response.json()