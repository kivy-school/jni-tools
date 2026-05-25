from typing import Any, ClassVar, overload
from java.nio.ByteBuffer import ByteBuffer
from java.nio.channels.CompletionHandler import CompletionHandler
from java.util.concurrent.Future import Future

class AsynchronousByteChannel:
    @overload
    def read(self, arg0: ByteBuffer, arg1: Any, arg2: CompletionHandler) -> None: ...
    @overload
    def read(self, arg0: ByteBuffer) -> Future: ...
    @overload
    def write(self, arg0: ByteBuffer, arg1: Any, arg2: CompletionHandler) -> None: ...
    @overload
    def write(self, arg0: ByteBuffer) -> Future: ...
