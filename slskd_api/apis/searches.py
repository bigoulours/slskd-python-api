from .base import *
import uuid
from typing import Optional

class SearchesApi(BaseApi):
    """
    Class that handles operations on searches.
    """

    def search_text(self,
                    searchText: str,
                    id: Optional[str] = None,
                    fileLimit: int = 10000,
                    filterResponses: bool = True,
                    maximumPeerQueueLength: int = 30,
                    minimumPeerUploadSpeed: int = 100000,
                    minimumResponseFileCount: int = 1,
                    responseLimit: int = 500,
                    searchTimeout: int = 5000
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
            "token": 0  # ToDo: understand what it does
        }
        response = requests.post(url, headers=self.header, json=data)
        return response.json()
    

    def get_all(self) -> list:
        """
        Gets the list of active and completed searches.
        """
        url = self.api_url + '/searches'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def state(self, id: str, includeResponses: bool = False) -> dict:
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
        response = requests.get(url, headers=self.header, params=params)
        return response.json()
    

    def stop(self, id: str) -> bool:
        """
        Stops the search corresponding to the specified id.

        :return: True if successful.
        """
        url = self.api_url + f'/searches/{id}'
        response = requests.put(url, headers=self.header)
        return response.ok
    

    def delete(self, id: str):
        """
        Deletes the search corresponding to the specified id.

        :return: True if successful.
        """
        url = self.api_url + f'/searches/{id}'
        response = requests.delete(url, headers=self.header)
        return response.ok
    

    def search_responses(self, id: str) -> list:
        """
        Gets search responses corresponding to the specified id.
        """
        url = self.api_url + f'/searches/{id}/responses'
        response = requests.get(url, headers=self.header)
        return response.json()