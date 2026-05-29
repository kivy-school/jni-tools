from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.gesture.GestureLibrary import GestureLibrary
from android.os.ParcelFileDescriptor import ParcelFileDescriptor
from java.io.File import File

class GestureLibraries:
    @staticmethod
    def fromRawResource(p0: Context, p1: int) -> GestureLibrary: ...
    @staticmethod
    def fromFileDescriptor(p0: ParcelFileDescriptor) -> GestureLibrary: ...
    @staticmethod
    def fromPrivateFile(p0: Context, p1: str) -> GestureLibrary: ...
    @overload
    @staticmethod
    def fromFile(p0: File) -> GestureLibrary: ...
    @overload
    @staticmethod
    def fromFile(p0: str) -> GestureLibrary: ...
