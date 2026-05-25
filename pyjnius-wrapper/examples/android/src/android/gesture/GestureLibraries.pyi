from typing import Any, ClassVar, overload
from android.content.Context import Context
from android.gesture.GestureLibrary import GestureLibrary
from android.os.ParcelFileDescriptor import ParcelFileDescriptor
from java.io.File import File

class GestureLibraries:
    @overload
    @staticmethod
    def fromFile(arg0: str) -> GestureLibrary: ...
    @overload
    @staticmethod
    def fromFile(arg0: File) -> GestureLibrary: ...
    @staticmethod
    def fromFileDescriptor(arg0: ParcelFileDescriptor) -> GestureLibrary: ...
    @staticmethod
    def fromPrivateFile(arg0: Context, arg1: str) -> GestureLibrary: ...
    @staticmethod
    def fromRawResource(arg0: Context, arg1: int) -> GestureLibrary: ...
