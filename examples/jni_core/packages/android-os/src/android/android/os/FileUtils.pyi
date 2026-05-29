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
    def copy(p0: FileDescriptor, p1: FileDescriptor, p2: CancellationSignal, p3: Executor, p4: Any) -> int: ...
    @overload
    @staticmethod
    def copy(p0: InputStream, p1: OutputStream) -> int: ...
    @overload
    @staticmethod
    def copy(p0: InputStream, p1: OutputStream, p2: CancellationSignal, p3: Executor, p4: Any) -> int: ...
    @overload
    @staticmethod
    def copy(p0: FileDescriptor, p1: FileDescriptor) -> int: ...
    @overload
    @staticmethod
    def closeQuietly(p0: AutoCloseable) -> None: ...
    @overload
    @staticmethod
    def closeQuietly(p0: FileDescriptor) -> None: ...

    class ProgressListener:
        def onProgress(self, p0: int) -> None: ...
