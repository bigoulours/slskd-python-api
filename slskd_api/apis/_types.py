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

from typing import TypedDict, NotRequired, Literal, TypeAlias, Union

# ApplicationApi:
class AppVersion(TypedDict):
    """
    TypedDict describing application version. Returned by :py:meth:`~slskd_api.apis.ApplicationApi.check_updates`.
    """
    full: str
    current: str
    latest: str
    isUpdateAvailable: bool
    isCanary: bool
    isDevelopment: bool


class AppState(TypedDict):
    """
    TypedDict describing application state. Returned by :py:meth:`~slskd_api.apis.ApplicationApi.state`.
    """
    version: AppVersion
    pendingReconnect: bool
    pendingRestart: bool
    server: 'ServerState'
    # TODO: describe as TypedDict?
    connectionWatchdog: dict
    relay: dict
    user: dict
    distributedNetwork: dict
    shares: dict
    rooms: list[str] # list of joined rooms
    users: list


# ConversationsApi
MessageDirection: TypeAlias = Literal["Out", "In"]

class Message(TypedDict):
    """
    TypedDict describing a message. Element of :py:class:`~Conversation`.
    """
    timestamp: str
    id: int
    username: str
    direction: MessageDirection
    message: str
    isAcknowledged: bool
    wasReplayed: bool

class Conversation(TypedDict):
    """
    TypedDict describing a conversation. Returned by :py:meth:`~slskd_api.apis.ConversationsApi.get`.
    """
    username: str
    isActive: bool
    unAcknowledgedMessageCount: int
    hasUnAcknowledgedMessages: bool
    messages: NotRequired[list[Message]] # not included in response from get_all


# EventsApi:
EventType: TypeAlias = Literal["DownloadFileComplete", "DownloadDirectoryComplete", "UploadFileComplete", "PrivateMessageReceived", "RoomMessageReceived", "Noop"]

class Event(TypedDict):
    """
    TypedDict describing an event. Single element of list returned by :py:meth:`~slskd_api.apis.EventsApi.get`.
    """
    timestamp: str # ISO date
    type: EventType
    data: str # event attributes as json
    id: str


# FilesApi:
class File(TypedDict):
    """
    TypedDict describing a file in the `downloads` or `incomplete` folder. See :py:class:`~slskd_api.apis.FilesApi`.
    """
    name: str
    fullname: str
    length: int
    attributes: str
    createdAt: str
    modifiedAt: str
    

class Directory(TypedDict):
    """
    TypedDict describing a directory in the `downloads` or `incomplete` folder. See :py:class:`~slskd_api.apis.FilesApi`.
    """
    name: str
    fullname: str
    attributes: str
    createdAt: str
    modifiedAt: str
    files: list[File]
    directories: list['Directory']


# LogsApi:
class LogEntry(TypedDict):
    """
    TypedDict describing a log entry. Single element of list returned by :py:meth:`~slskd_api.apis.LogsApi.get`.
    """
    timestamp: str
    context: str
    level: str
    message: str


# RoomsApi:
class RoomMessage(TypedDict):
    """
    TypedDict describing a message in a room. See :py:class:`~Room`.
    """
    timestamp: str
    username: str
    message: str
    roomName: str

class RoomInfo(TypedDict):
    """
    TypedDict describing room info.
    """
    name: str
    userCount: int
    isPrivate: bool
    isOwned: bool
    isModerated: bool
    
class RoomUser(TypedDict):
    """
    TypedDict describing a room user.
    """
    averageSpeed: int
    countryCode: str
    directoryCount: int
    fileCount: int
    slotsFree: int
    status: 'UserPresence'
    uploadCount: int
    username: str
    
    
class Room(TypedDict):
    """
    TypedDict describing a room. Returned by :py:meth:`~slskd_api.apis.RoomsApi.join`
    and :py:meth:`~slskd_api.apis.RoomsApi.get_joined`.
    """
    name: str
    isPrivate: bool
    users: list[RoomUser]
    messages: list[RoomMessage]


# SearchApi:
class SearchFile(TypedDict):
    """
    TypedDict describing a single search file result. Element found in :py:class:`~SearchResponseItem`.
    """
    filename: str
    size: int
    code: int
    isLocked: bool
    extension: str
    bitRate: NotRequired[int] # for lossy format
    bitDepth: NotRequired[int] # for lossless format
    length: NotRequired[int] # in sec
    sampleRate: NotRequired[int] # in Hz

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
    endedAt: NotRequired[str]
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


# ServerApi:
class ServerState(TypedDict):
    """
    TypedDict describing server state. Returned by :py:meth:`~slskd_api.apis.ServerApi.state`.
    """
    address: str
    ipEndPoint: str
    state: Literal["Connected, LoggedIn", "Disconnected"] # TODO: not sure if complete, but haven't figured out others.
    isConnected: bool
    isConnecting: bool
    isLoggedIn: bool
    isLoggingIn: bool
    isTransitioning: bool  


# SessionApi:
class SessionStatus(TypedDict):
    """
    TypedDict describing session status. Returned by :py:meth:`~slskd_api.apis.SessionApi.login`.
    """
    expires: int
    issued: int
    name: str
    notBefore: int
    token: str
    tokenType: str


# SharesApi:
class ShareInfo(TypedDict):
    """
    TypedDict describing a shared directory. Returned by :py:meth:`~slskd_api.apis.SharesApi.get`.
    """
    id: str
    alias: str
    isExcluded: bool
    localPath: str
    raw: str
    remotePath: str
    directories: int
    files: int

class Shares(TypedDict):
    """
    TypedDict describing all shares (local or from relays). Returned by :py:meth:`~slskd_api.apis.SharesApi.get_all`.
    """
    local: list[ShareInfo]


# TransfersApi
class TransferedFile(TypedDict):
    """
    TypedDict describing a transfered file. Element found in :py:class:`~TransferedDirectory`.
    """
    id: str
    username: str
    direction: Literal["Download", "Upload"]
    filename: str 
    size: int
    startOffset: int
    state: str
    requestedAt: str
    enqueuedAt: str
    startedAt: str
    endedAt: str
    bytesTransferred: int
    averageSpeed: float
    bytesRemaining: int
    elapsedTime: str
    percentComplete: float
    remainingTime: str
    

class TransferedDirectory(TypedDict):
    """
    TypedDict describing a transfered directory. Element found in :py:class:`~Transfer`.
    """
    directory: str  # remote directory
    fileCount: int
    files: list[TransferedFile]


class Transfer(TypedDict):
    """
    TypedDict describing transfer(s) to/from a given user. See :py:class:`~slskd_api.apis.TransfersApi`.
    """
    username: str
    directories: list[TransferedDirectory]

    
# UsersApi:
class UserAddress(TypedDict):
    """
    TypedDict describing a user IP address. Returned by :py:meth:`~slskd_api.apis.UsersApi.address`.
    """
    addressFamily: str
    address: str
    port: int
    
class BrowsingStatus(TypedDict):
    """
    TypedDict describing browsing status of a user's shares. Returned by :py:meth:`~slskd_api.apis.UsersApi.browsing_status`.
    """
    bytesTransferred: int
    bytesRemaining: int
    percentComplete: int
    size: int
    username: str
    
class UserInfo(TypedDict):
    """
    TypedDict describing user info. Returned by :py:meth:`~slskd_api.apis.UsersApi.info`.
    """
    description: str
    hasFreeUploadSlot: bool
    hasPicture: bool
    picture: str
    queueLength: int
    uploadSlots: int

UserPresence: TypeAlias = Literal["Offline", "Away", "Online"]

class UserStatus(TypedDict):
    """
    TypedDict describing user status. Returned by :py:meth:`~slskd_api.apis.UsersApi.status`.
    """
    isPrivileged: bool
    presence: UserPresence

class FileAttribute(TypedDict):
    """
    TypedDict describing a file attribute. Defined attributes are added as new keys to :py:class:`~UserFile`.
    """
    type: str
    value: int

class UserFile(TypedDict):
    """
    TypedDict describing a user file. Found in :py:class:`~UserDirectory`.
    """
    attributeCount: int
    attributes: list[FileAttribute]
    code: int
    extension: str
    filename: str
    size: int # in Byte
    
class UserDirectory(TypedDict):
    """
    TypedDict describing a user directory either locked or not. See :py:class:`~UserRootDir`.
    """
    name: str
    fileCount: int
    files: list[UserFile]
    
class UserRootDir(TypedDict):
    """
    TypedDict describing the root of a user's shares. Returned by :py:meth:`~slskd_api.apis.UsersApi.browse`.
    """
    directories: list[UserDirectory]
    directoryCount: int
    lockedDirectories: list[UserDirectory]
    lockedDirectoryCount: int