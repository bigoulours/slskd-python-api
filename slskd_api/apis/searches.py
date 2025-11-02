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
import uuid
import time
from typing import Optional, TypedDict


class SearchFile(TypedDict):
    """
    TypedDict describing a single search file result. Element found in :py:class:`~slskd_api.apis.searches.SearchResponseItem`.
    """
    filename: str
    size: int
    code: int
    isLocked: bool
    extension: str
    bitRate: int # for lossy format
    bitDepth: int # for lossless format
    length: int # in sec
    sampleRate: int # in Hz

class SearchResponseItem(TypedDict):
    """
    TypedDict describing a search response item. Single element of list returned by :py:meth:`~slskd_api.apis.SearchesApi.search_responses`.
    """
    fileCount: int
    files: list[SearchFile]
    hasFreeUploadSlot: bool
    lockedFileCount: int
    lockedFiles: list[SearchFile]
    queueLength: int
    token: int
    uploadSpeed: int
    username: str

class SearchState(TypedDict):
    """
    TypedDict describing search state. Returned by :py:meth:`~slskd_api.apis.SearchesApi.state`.
    """
    endedAt: str
    fileCount: int
    id: str
    isComplete: bool
    lockedFileCount: int
    responseCount: int
    responses: list[SearchResponseItem]
    searchText: str
    startedAt: str  # ISO date
    state: str
    token: int


class SearchesApi(BaseApi):
    """
    Class that handles operations on searches.
    """

    def search_text(self,
                    searchText: str,
                    id: Optional[str] = None,
                    fileLimit: int = 10000,
                    filterResponses: bool = True,
                    maximumPeerQueueLength: int = 1000000,
                    minimumPeerUploadSpeed: int = 0,
                    minimumResponseFileCount: int = 1,
                    responseLimit: int = 100,
                    searchTimeout: int = 15000
        ) -> dict:
        """
        Performs a search for the specified request.

        :param searchText: Search query
        :param id: uuid of the search. One will be generated if None.
        :param fileLimit: Max number of file results
        :param filterResponses: Filter unreachable users from the results
        :param maximumPeerQueueLength: Max queue length
        :param minimumPeerUploadSpeed: Min upload speed in bit/s
        :param minimumResponseFileCount: Min number of matching files per user
        :param responseLimit: Max number of users results
        :param searchTimeout: Search timeout in ms
        :return: Info about the search (no results!)
        """

        url = self.api_url + '/searches'

        try:
            id = str(uuid.UUID(id)) # check if given id is a valid uuid
        except:
            id = str(uuid.uuid1())  # otherwise generate a new one

        data = {
            "id": id,
            "fileLimit": fileLimit,
            "filterResponses": filterResponses,
            "maximumPeerQueueLength": maximumPeerQueueLength,
            "minimumPeerUploadSpeed": minimumPeerUploadSpeed,
            "minimumResponseFileCount": minimumResponseFileCount,
            "responseLimit": responseLimit,
            "searchText": searchText,
            "searchTimeout": searchTimeout,
        }
        response = self.session.post(url, json=data)
        return response.json()
    

    def get_all(self) -> list:
        """
        Gets the list of active and completed searches.
        """
        url = self.api_url + '/searches'
        response = self.session.get(url)
        return response.json()
    

    def state(self, id: str, includeResponses: bool = False) -> SearchState:
        """
        Gets the state of the search corresponding to the specified id.

        :param id: uuid of the search.
        :param includeResponses: Include responses (search result list) in the returned dict
        :return: Info about the search
        """
        url = self.api_url + f'/searches/{id}'
        params = dict(
            includeResponses=includeResponses
        )
        response = self.session.get(url, params=params)
        return response.json()
    

    def stop(self, id: str) -> bool:
        """
        Stops the search corresponding to the specified id.

        :return: True if successful.
        """
        url = self.api_url + f'/searches/{id}'
        response = self.session.put(url)
        return response.ok
    
    def stop_all(self) -> None:
        """
        Stops all searches.

        :return: None. Throws error if not successful.
        """
        for search in self.get_all():
            ok = self.stop(search["id"])
            assert ok, f"stop failed on {search["filename"]}"
    

    def delete(self, id: str):
        """
        Deletes the search corresponding to the specified id.

        :return: True if successful.
        """
        url = self.api_url + f'/searches/{id}'
        response = self.session.delete(url)
        return response.ok
    
    def delete_all(self) -> None:
        """
        Deletes all searches.

        :return: None. Throws error if not successful.
        """
        for search in self.get_all():
            ok = self.delete(search["id"])
            assert ok, f"delete failed on {search["filename"]}"
    

    def search_responses(self, id: str) -> list[SearchResponseItem]:
        """
        Gets search responses corresponding to the specified id.
        """
        url = self.api_url + f'/searches/{id}/responses'
        response = self.session.get(url)
        return response.json()
    
    def wait_for_search(self, id: str, timeout: int = 10, interval: int = 0.5) -> None:
        """
        Waits for a search to complete, returning the search responses when complete.

        :param id: uuid of the search.
        :param timeout: Timeout (in secs) on which to error if the search has gone stagnant
              (NOTE: this is not the timeout of the overall search. It is the timeout for when no new results are provided.)
        :param interval: Interval (in secs) at which the query to `self.state` is performed.
        :return: None, when is complete, otherwise throws `TimeoutError`.
        """
        timeout_start = time.time()
        prev_results_cnt: int = 0
        while True:
            search_state = self.state(id)
            if search_state["isComplete"] and "Completed" in search_state["state"]:
                return
            if search_state["responseCount"] > prev_results_cnt:
                timeout_start = time.time()
                prev_results_cnt = search_state["responseCount"]
            if time.time() - timeout_start > timeout:
                raise TimeoutError("search timed out")
            time.sleep(interval)