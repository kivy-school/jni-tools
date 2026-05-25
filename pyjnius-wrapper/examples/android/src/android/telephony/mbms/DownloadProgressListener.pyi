from typing import Any, ClassVar, overload
from android.telephony.mbms.DownloadRequest import DownloadRequest
from android.telephony.mbms.FileInfo import FileInfo

class DownloadProgressListener:
    def __init__(self) -> None: ...
    def onProgressUpdated(self, arg0: DownloadRequest, arg1: FileInfo, arg2: int, arg3: int, arg4: int, arg5: int) -> None: ...
