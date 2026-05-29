from typing import Any, ClassVar, overload
from android.hardware.camera2.params.MultiResolutionStreamInfo import MultiResolutionStreamInfo
from android.media.ImageReader import ImageReader
from android.view.Surface import Surface
from java.util.concurrent.Executor import Executor

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class OnImageAvailableListener:
    """Forward declaration for ``android.media.ImageReader.OnImageAvailableListener``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.media.ImageReader.OnImageAvailableListener')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/media/ImageReader/OnImageAvailableListener
    """
    ...

class MultiResolutionImageReader:
    def __init__(self, arg0: list, arg1: int, arg2: int) -> None: ...
    def setOnImageAvailableListener(self, arg0: OnImageAvailableListener, arg1: Executor) -> None: ...
    def close(self) -> None: ...
    def finalize(self) -> None: ...
    def flush(self) -> None: ...
    def getSurface(self) -> Surface: ...
    def getStreamInfoForImageReader(self, arg0: ImageReader) -> MultiResolutionStreamInfo: ...
