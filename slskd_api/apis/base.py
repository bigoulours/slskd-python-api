import requests

class BaseApi:
    """
    Base class where api-url and headers are set for all requests.
    """

    def __init__(self, api_url: str, header: dict):
        self.api_url = api_url
        self.header = header