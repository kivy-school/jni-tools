from typing import Any, ClassVar, overload
from android.graphics.Bitmap import Bitmap
from android.graphics.Rect import Rect
from android.os.ParcelFileDescriptor import ParcelFileDescriptor
from java.io.FileDescriptor import FileDescriptor
from java.io.InputStream import InputStream

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Options:
    """Forward declaration for ``android.graphics.BitmapFactory.Options``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.graphics.BitmapFactory.Options')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/graphics/BitmapFactory/Options
    """
    ...

class BitmapRegionDecoder:
    @overload
    @staticmethod
    def newInstance(arg0: list[int], arg1: int, arg2: int, arg3: bool) -> "BitmapRegionDecoder": ...
    @overload
    @staticmethod
    def newInstance(arg0: list[int], arg1: int, arg2: int) -> "BitmapRegionDecoder": ...
    @overload
    @staticmethod
    def newInstance(arg0: FileDescriptor, arg1: bool) -> "BitmapRegionDecoder": ...
    @overload
    @staticmethod
    def newInstance(arg0: ParcelFileDescriptor) -> "BitmapRegionDecoder": ...
    @overload
    @staticmethod
    def newInstance(arg0: InputStream, arg1: bool) -> "BitmapRegionDecoder": ...
    @overload
    @staticmethod
    def newInstance(arg0: InputStream) -> "BitmapRegionDecoder": ...
    @overload
    @staticmethod
    def newInstance(arg0: str, arg1: bool) -> "BitmapRegionDecoder": ...
    @overload
    @staticmethod
    def newInstance(arg0: str) -> "BitmapRegionDecoder": ...
    def decodeRegion(self, arg0: Rect, arg1: Options) -> Bitmap: ...
    def getWidth(self) -> int: ...
    def getHeight(self) -> int: ...
    def recycle(self) -> None: ...
    def isRecycled(self) -> bool: ...
    def finalize(self) -> None: ...
