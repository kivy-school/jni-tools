from typing import Any, ClassVar, overload
from android.os.CancellationSignal import CancellationSignal
from java.io.FileDescriptor import FileDescriptor
from java.io.InputStream import InputStream
from java.io.OutputStream import OutputStream
from java.lang.AutoCloseable import AutoCloseable
from java.util.concurrent.Executor import Executor

class FileUtils:
    @overload
    @staticmethod
    def copy(arg0: InputStream, arg1: OutputStream) -> int: ...
    @overload
    @staticmethod
    def copy(arg0: InputStream, arg1: OutputStream, arg2: CancellationSignal, arg3: Executor, arg4: "ProgressListener") -> int: ...
    @overload
    @staticmethod
    def copy(arg0: FileDescriptor, arg1: FileDescriptor) -> int: ...
    @overload
    @staticmethod
    def copy(arg0: FileDescriptor, arg1: FileDescriptor, arg2: CancellationSignal, arg3: Executor, arg4: "ProgressListener") -> int: ...
    @overload
    @staticmethod
    def closeQuietly(arg0: AutoCloseable) -> None: ...
    @overload
    @staticmethod
    def closeQuietly(arg0: FileDescriptor) -> None: ...

    class ProgressListener:
        def onProgress(self, arg0: int) -> None: ...
