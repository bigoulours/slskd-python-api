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
    # TODO: describe as TypedDict
    connectionWatchdog: dict
    relay: dict
    user: dict
    distributedNetwork: dict
    shares: dict
    rooms: list
    users: list


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


# SharesApi:
class SharedDir(TypedDict):
    """
    TypedDict describing a shared directory. Returned :py:meth:`~slskd_api.apis.SharesApi.get`.
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
    TypedDict describing all shares (local or from relays). Returned :py:meth:`~slskd_api.apis.SharesApi.get_all`.
    """
    local: list[SharedDir]


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
    TypedDict describing transfer(s) to/from a given user. See :py:class:`~slskd_api.apis.TransferApi`.
    """
    username: str
    directories: list[TransferedDirectory]

    
# UsersApi:
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