from typing import Any, ClassVar, overload
from java.nio.ByteBuffer import ByteBuffer
from java.nio.channels.CompletionHandler import CompletionHandler
from java.util.concurrent.Future import Future

class AsynchronousByteChannel:
    @overload
    def write(self, p0: ByteBuffer) -> Future: ...
    @overload
    def write(self, p0: ByteBuffer, p1: Any, p2: CompletionHandler) -> None: ...
    @overload
    def read(self, p0: ByteBuffer) -> Future: ...
    @overload
    def read(self, p0: ByteBuffer, p1: Any, p2: CompletionHandler) -> None: ...
