from typing import Any, ClassVar, overload
from android.content.res.Resources import Resources
from android.graphics.Bitmap import Bitmap
from android.graphics.ColorSpace import ColorSpace
from android.graphics.Rect import Rect
from android.util.TypedValue import TypedValue
from java.io.FileDescriptor import FileDescriptor
from java.io.InputStream import InputStream

# Forward declarations for Java types we do not wrap.
# Bound as empty classes so annotations resolve in the IDE.
class Config:
    """Forward declaration for ``android.graphics.Bitmap.Config``.

    This Java type is referenced by the wrapper but is not itself
    wrapped by pyjnius-wrap. At runtime pyjnius will hand you a
    live ``autoclass('android.graphics.Bitmap.Config')`` proxy; this empty class exists
    purely so static type checkers and IDEs can resolve the name.

    See: https://developer.android.com/reference/android/graphics/Bitmap/Config
    """
    ...

class BitmapFactory:
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def decodeFile(arg0: str, arg1: "Options") -> Bitmap: ...
    @overload
    @staticmethod
    def decodeFile(arg0: str) -> Bitmap: ...
    @staticmethod
    def decodeResourceStream(arg0: Resources, arg1: TypedValue, arg2: InputStream, arg3: Rect, arg4: "Options") -> Bitmap: ...
    @overload
    @staticmethod
    def decodeResource(arg0: Resources, arg1: int, arg2: "Options") -> Bitmap: ...
    @overload
    @staticmethod
    def decodeResource(arg0: Resources, arg1: int) -> Bitmap: ...
    @overload
    @staticmethod
    def decodeByteArray(arg0: list[int], arg1: int, arg2: int, arg3: "Options") -> Bitmap: ...
    @overload
    @staticmethod
    def decodeByteArray(arg0: list[int], arg1: int, arg2: int) -> Bitmap: ...
    @overload
    @staticmethod
    def decodeStream(arg0: InputStream, arg1: Rect, arg2: "Options") -> Bitmap: ...
    @overload
    @staticmethod
    def decodeStream(arg0: InputStream) -> Bitmap: ...
    @overload
    @staticmethod
    def decodeFileDescriptor(arg0: FileDescriptor, arg1: Rect, arg2: "Options") -> Bitmap: ...
    @overload
    @staticmethod
    def decodeFileDescriptor(arg0: FileDescriptor) -> Bitmap: ...

    class Options:
        inBitmap: Bitmap
        inDensity: int
        inDither: bool
        inInputShareable: bool
        inJustDecodeBounds: bool
        inMutable: bool
        inPreferQualityOverSpeed: bool
        inPreferredColorSpace: ColorSpace
        inPreferredConfig: Config
        inPremultiplied: bool
        inPurgeable: bool
        inSampleSize: int
        inScaled: bool
        inScreenDensity: int
        inTargetDensity: int
        inTempStorage: list[int]
        mCancel: bool
        outColorSpace: ColorSpace
        outConfig: Config
        outHeight: int
        outMimeType: str
        outWidth: int
        def __init__(self) -> None: ...
        def requestCancelDecode(self) -> None: ...
