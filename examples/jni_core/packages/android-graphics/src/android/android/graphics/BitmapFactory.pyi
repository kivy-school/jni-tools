from typing import Any, ClassVar, overload
from android.content.res.Resources import Resources
from android.graphics.Bitmap import Bitmap
from android.graphics.ColorSpace import ColorSpace
from android.graphics.Rect import Rect
from android.util.TypedValue import TypedValue
from java.io.FileDescriptor import FileDescriptor
from java.io.InputStream import InputStream

class BitmapFactory:
    def __init__(self) -> None: ...
    @overload
    @staticmethod
    def decodeFileDescriptor(p0: FileDescriptor) -> Bitmap: ...
    @overload
    @staticmethod
    def decodeFileDescriptor(p0: FileDescriptor, p1: Rect, p2: Any) -> Bitmap: ...
    @overload
    @staticmethod
    def decodeResource(p0: Resources, p1: int, p2: Any) -> Bitmap: ...
    @overload
    @staticmethod
    def decodeResource(p0: Resources, p1: int) -> Bitmap: ...
    @staticmethod
    def decodeResourceStream(p0: Resources, p1: TypedValue, p2: InputStream, p3: Rect, p4: Any) -> Bitmap: ...
    @overload
    @staticmethod
    def decodeStream(p0: InputStream, p1: Rect, p2: Any) -> Bitmap: ...
    @overload
    @staticmethod
    def decodeStream(p0: InputStream) -> Bitmap: ...
    @overload
    @staticmethod
    def decodeByteArray(p0: Any, p1: int, p2: int) -> Bitmap: ...
    @overload
    @staticmethod
    def decodeByteArray(p0: Any, p1: int, p2: int, p3: Any) -> Bitmap: ...
    @overload
    @staticmethod
    def decodeFile(p0: str, p1: Any) -> Bitmap: ...
    @overload
    @staticmethod
    def decodeFile(p0: str) -> Bitmap: ...

    class Options:
        inBitmap: Bitmap
        inDensity: int
        inDither: bool
        inInputShareable: bool
        inJustDecodeBounds: bool
        inMutable: bool
        inPreferQualityOverSpeed: bool
        inPreferredColorSpace: ColorSpace
        inPreferredConfig: Any
        inPremultiplied: bool
        inPurgeable: bool
        inSampleSize: int
        inScaled: bool
        inScreenDensity: int
        inTargetDensity: int
        inTempStorage: Any
        mCancel: bool
        outColorSpace: ColorSpace
        outConfig: Any
        outHeight: int
        outMimeType: str
        outWidth: int
        def __init__(self) -> None: ...
        def requestCancelDecode(self) -> None: ...
