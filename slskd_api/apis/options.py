from .base import *

class OptionsApi(BaseApi):
    """
    This class contains the methods to interact with the Options API.
    """

    def get(self) -> dict:
        """
        Gets the current application options.
        """
        url = self.api_url + '/options'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def get_startup(self) -> dict:
        """
        Gets the application options provided at startup.
        """
        url = self.api_url + '/options/startup'
        response = requests.get(url, headers=self.header)
        return response.json()

  
    def debug(self) -> str:
        """
        Gets the debug view of the current application options.
        debug and remote_configuration must be set to true.
        Only works with token (usr/pwd login). 'Unauthorized' with API-Key.
        """
        url = self.api_url + '/options/debug'
        response = requests.get(url, headers=self.header)
        return response.json()


    def yaml_location(self) -> str:
        """
        Gets the path of the yaml config file. remote_configuration must be set to true.
        Only works with token (usr/pwd login). 'Unauthorized' with API-Key.
        """
        url = self.api_url + '/options/yaml/location'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def download_yaml(self) -> str:
        """
        Gets the content of the yaml config file as text. remote_configuration must be set to true.
        Only works with token (usr/pwd login). 'Unauthorized' with API-Key.
        """
        url = self.api_url + '/options/yaml'
        response = requests.get(url, headers=self.header)
        return response.json()
    

    def upload_yaml(self, yaml_content: str) -> bool:
        """
        Sets the content of the yaml config file. remote_configuration must be set to true.
        Only works with token (usr/pwd login). 'Unauthorized' with API-Key.

        :return: True if successful.
        """
        url = self.api_url + '/options/yaml'
        response = requests.post(url, headers=self.header, json=yaml_content)
        return response.ok
    

    def validate_yaml(self, yaml_content: str) -> str:
        """
        Validates the provided yaml string. remote_configuration must be set to true.
        Only works with token (usr/pwd login). 'Unauthorized' with API-Key.

        :return: Empty string if validation successful. Error message otherwise.
        """
        url = self.api_url + '/options/yaml/validate'
        response = requests.post(url, headers=self.header, json=yaml_content)
        return response.text