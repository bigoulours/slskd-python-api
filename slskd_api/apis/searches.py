from .base import *
import uuid

class SearchesApi(BaseApi):
    """
    Class that handles operations on searches.
    """

    def search_text(self,
                    searchText,
                    id=None,
                    fileLimit=10000,
                    filterResponses=True,
                    maximumPeerQueueLength=10,
                    minimumPeerUploadSpeed=0,
                    minimumResponseFileCount=1,
                    responseLimit=500,
                    searchTimeout=5000 # in ms
        ):
        """
        Performs a search for the specified request.
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
            "token": 0
        }
        response = requests.post(url, headers=self.header, json=data)
        return response.json()
    

    def get_all(self):
        """
        Gets the list of active and completed searches.
        """
        url = self.api_url + '/searches'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def state(self, id, includeResponses=False):
        """
        Gets the state of the search corresponding to the specified id.
        """
        url = self.api_url + f'/searches/{id}'
        params = dict(
            includeResponses=includeResponses
        )
        response = requests.get(url, headers=self.header, params=params)
        return response.json()
    

    def stop(self, id):
        """
        Stops the search corresponding to the specified id.
        """
        url = self.api_url + f'/searches/{id}'
        response = requests.put(url, headers=self.header)
        return response.ok
    

    def delete(self, id):
        """
        Deletes the search corresponding to the specified id.
        """
        url = self.api_url + f'/searches/{id}'
        response = requests.delete(url, headers=self.header)
        return response.ok
    

    def search_responses(self, id):
        """
        Gets search responses corresponding to the specified id.
        """
        url = self.api_url + f'/searches/{id}/responses'
        response = requests.get(url, headers=self.header)
        return response.json()