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

class FilesApi(BaseApi):
    """
    This class contains the methods to interact with the Files API.
    In order to delete files/directory you need to set `remoteFileManagement: true` in `slskd.yml`.
    base64 names can be obtained with `base64.encodebytes(<name_as_str>.encode()).decode()`
    """

    def get_downloads_dir(self, recursive: bool = False) -> Directory:
        """
        Lists the contents of the downloads directory.
        
        :param recursive: whether to recursively list subdirectories and files.
        """
        url = self.api_url + '/files/downloads/directories'
        params = dict(
            recursive=recursive
        )
        response = self.session.get(url, params=params)
        return response.json()
    

    def get_downloaded_directory(self, base64SubdirectoryName: str, recursive: bool = False) -> Directory:
        """
        Lists the contents of the specified subdirectory within the downloads directory.
        
        :param recursive: whether to recursively list subdirectories and files.
        """
        url = self.api_url + '/files/downloads/directories/' + base64SubdirectoryName
        params = dict(
            recursive=recursive
        )
        response = self.session.get(url, params=params)
        return response.json()


    def delete_downloaded_directory(self, base64SubdirectoryName: str) -> bool:
        """
        Deletes the specified subdirectory within the downloads directory.
        """
        url = self.api_url + '/files/downloads/directories/' + base64SubdirectoryName
        response = self.session.delete(url)
        return response.ok


    def delete_downloaded_file(self, base64FileName: str) -> bool:
        """
        Deletes the specified file within the downloads directory.
        """
        url = self.api_url + '/files/downloads/directories/' + base64FileName
        response = self.session.delete(url)
        return response.ok
    
    
    def get_incomplete_dir(self, recursive: bool = False) -> Directory:
        """
        Lists the contents of the incomplete directory.
        
        :param recursive: whether to recursively list subdirectories and files.
        """
        url = self.api_url + '/files/incomplete/directories'
        params = dict(
            recursive=recursive
        )
        response = self.session.get(url, params=params)
        return response.json()
    

    def get_incomplete_directory(self, base64SubdirectoryName: str, recursive: bool = False) -> Directory:
        """
        Lists the contents of the specified subdirectory within the incomplete directory.
        
        :param recursive: whether to recursively list subdirectories and files.
        """
        url = self.api_url + '/files/incomplete/directories/' + base64SubdirectoryName
        params = dict(
            recursive=recursive
        )
        response = self.session.get(url, params=params)
        return response.json()


    def delete_incomplete_directory(self, base64SubdirectoryName: str) -> bool:
        """
        Deletes the specified subdirectory within the incomplete directory.
        """
        url = self.api_url + '/files/incomplete/directories/' + base64SubdirectoryName
        response = self.session.delete(url)
        return response.ok


    def delete_incomplete_file(self, base64FileName: str) -> bool:
        """
        Deletes the specified file within the incomplete directory.
        """
        url = self.api_url + '/files/incomplete/directories/' + base64FileName
        response = self.session.delete(url)
        return response.ok