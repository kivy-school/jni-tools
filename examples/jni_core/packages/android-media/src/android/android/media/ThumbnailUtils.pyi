from typing import Any, ClassVar, overload
from android.graphics.Bitmap import Bitmap
from android.os.CancellationSignal import CancellationSignal
from android.util.Size import Size
from java.io.File import File

class ThumbnailUtils:
    OPTIONS_RECYCLE_INPUT: ClassVar[int]
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def createAudioThumbnail(p0: str, p1: int) -> Bitmap: ...
    @overload
    @staticmethod
    def createAudioThumbnail(p0: File, p1: Size, p2: CancellationSignal) -> Bitmap: ...
    @overload
    @staticmethod
    def createImageThumbnail(p0: str, p1: int) -> Bitmap: ...
    @overload
    @staticmethod
    def createImageThumbnail(p0: File, p1: Size, p2: CancellationSignal) -> Bitmap: ...
    @overload
    @staticmethod
    def createVideoThumbnail(p0: File, p1: Size, p2: CancellationSignal) -> Bitmap: ...
    @overload
    @staticmethod
    def createVideoThumbnail(p0: str, p1: int) -> Bitmap: ...
    @overload
    @staticmethod
    def extractThumbnail(p0: Bitmap, p1: int, p2: int) -> Bitmap: ...
    @overload
    @staticmethod
    def extractThumbnail(p0: Bitmap, p1: int, p2: int, p3: int) -> Bitmap: ...
