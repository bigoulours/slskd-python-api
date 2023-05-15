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
    e.g.:
    ```
    slskd = slskd_api.SlskdClient(host, api_key, url_base)
    app_status = slskd.application.state()
    ```
    """

    def __init__(self, host, api_key, url_base='/'):
        api_url = reduce(urljoin, [host, f'{url_base}/', f'api/{API_VERSION}'])
        header = {
            'accept': '*/*',
            'X-API-Key': api_key
        }
        base_args = (api_url, header)
        
        self.application = ApplicationApi(*base_args)
        self.conversations = ConversationsApi(*base_args)
        self.logs = LogsApi(*base_args)
        self.options = OptionsApi(*base_args)
        self.rooms = RoomsApi(*base_args)
        self.searches = SearchesApi(*base_args)
        self.server = ServerApi(*base_args)
        self.session = SessionApi(*base_args)
        self.transfers = TransfersApi(*base_args)
        self.users = UsersApi(*base_args)
    

class MetricsApi:
    """
    Getting the metrics works with a different end point. Default: <slskd_url>:5030/metrics.
    Metrics should be first activated in slskd config file.
    User/pass is independent from the main application and default value (slskd:slskd) should be changed.
    e.g.:
    ```
    metrics_conn = slskd_api.MetricsApi(host, metrics_usr='slskd', metrics_pwd='slskd')
    metrics = metrics_conn.get()
    ```
    """

    def __init__(self, host, metrics_usr=None, metrics_pwd=None, metrics_url_base='/metrics'):
        self.metrics_url = urljoin(host, metrics_url_base)
        basic_auth = b64encode(bytes(f'{metrics_usr}:{metrics_pwd}', 'utf-8'))
        self.header = {
            'accept': '*/*',
            'Authorization': f'Basic {basic_auth.decode()}' 
        }

    def get(self):
        response = requests.get(self.metrics_url, headers=self.header)
        return response.text
