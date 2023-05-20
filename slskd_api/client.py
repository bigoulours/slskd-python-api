API_VERSION = 'v0'

import requests
from urllib.parse import urljoin
from functools import reduce
from base64 import b64encode
from slskd_api.apis import *

class SlskdClient:
    """
    The main class that allows access to the different APIs of a slskd instance.
    An API-Key with appropriate permissions (`readwrite` for most use cases) must be set in slskd config file.
    Alternatively, provide your username and password.
    Usage::
        slskd = slskd_api.SlskdClient(host, api_key, url_base)
        app_status = slskd.application.state()
    """

    def __init__(self,
                 host: str,
                 api_key: str = None,
                 url_base: str = '/',
                 username: str = None,
                 password: str = None,
    ):
        api_url = reduce(urljoin, [host, f'{url_base}/', f'api/{API_VERSION}'])
     
        header = {'accept': '*/*'}

        if api_key:
            header['X-API-Key'] = api_key
        elif username and password:
            header['Authorization'] = 'Bearer ' + \
                            SessionApi(api_url, header).login(username, password)['token']
        else:
            raise ValueError('Please provide an API-Key or a valid username/password pair.')
        
        base_args = (api_url, header)
        
        self.application = ApplicationApi(*base_args)
        self.conversations = ConversationsApi(*base_args)
        self.logs = LogsApi(*base_args)
        self.options = OptionsApi(*base_args)
        self.public_chat = PublicChatApi(*base_args)
        self.relay = RelayApi(*base_args)
        self.rooms = RoomsApi(*base_args)
        self.searches = SearchesApi(*base_args)
        self.server = ServerApi(*base_args)
        self.session = SessionApi(*base_args)
        self.shares = SharesApi(*base_args)
        self.transfers = TransfersApi(*base_args)
        self.users = UsersApi(*base_args)
    

class MetricsApi:
    """
    Getting the metrics works with a different endpoint. Default: <slskd_url>:5030/metrics.
    Metrics should be first activated in slskd config file.
    User/pass is independent from the main application and default value (slskd:slskd) should be changed.
    Usage::
        metrics_api = slskd_api.MetricsApi(host, metrics_usr='slskd', metrics_pwd='slskd')
        metrics = metrics_api.get()
    """

    def __init__(self,
                 host: str,
                 metrics_usr: str = 'slskd',
                 metrics_pwd: str = 'slskd',
                 metrics_url_base: str = '/metrics'
    ):
        self.metrics_url = urljoin(host, metrics_url_base)
        basic_auth = b64encode(bytes(f'{metrics_usr}:{metrics_pwd}', 'utf-8'))
        self.header = {
            'accept': '*/*',
            'Authorization': f'Basic {basic_auth.decode()}' 
        }

    def get(self) -> str:
        """
        Gets the Prometheus metrics as text.
        """
        response = requests.get(self.metrics_url, headers=self.header)
        return response.text
