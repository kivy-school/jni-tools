from typing import Any, ClassVar, overload
from android.telephony.mbms.DownloadRequest import DownloadRequest
from android.telephony.mbms.FileInfo import FileInfo

class DownloadProgressListener:
    def __init__(self) -> None: ...
    def onProgressUpdated(self, p0: DownloadRequest, p1: FileInfo, p2: int, p3: int, p4: int, p5: int) -> None: ...
