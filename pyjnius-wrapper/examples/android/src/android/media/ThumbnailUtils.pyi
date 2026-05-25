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
    def createAudioThumbnail(arg0: str, arg1: int) -> Bitmap: ...
    @overload
    @staticmethod
    def createAudioThumbnail(arg0: File, arg1: Size, arg2: CancellationSignal) -> Bitmap: ...
    @overload
    @staticmethod
    def createImageThumbnail(arg0: str, arg1: int) -> Bitmap: ...
    @overload
    @staticmethod
    def createImageThumbnail(arg0: File, arg1: Size, arg2: CancellationSignal) -> Bitmap: ...
    @overload
    @staticmethod
    def createVideoThumbnail(arg0: str, arg1: int) -> Bitmap: ...
    @overload
    @staticmethod
    def createVideoThumbnail(arg0: File, arg1: Size, arg2: CancellationSignal) -> Bitmap: ...
    @overload
    @staticmethod
    def extractThumbnail(arg0: Bitmap, arg1: int, arg2: int) -> Bitmap: ...
    @overload
    @staticmethod
    def extractThumbnail(arg0: Bitmap, arg1: int, arg2: int, arg3: int) -> Bitmap: ...
