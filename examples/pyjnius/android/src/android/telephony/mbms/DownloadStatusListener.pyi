from typing import Any, ClassVar, overload
from android.telephony.mbms.DownloadRequest import DownloadRequest
from android.telephony.mbms.FileInfo import FileInfo

class DownloadStatusListener:
    def __init__(self) -> None: ...
    def onStatusUpdated(self, arg0: DownloadRequest, arg1: FileInfo, arg2: int) -> None: ...
