from typing import Any, ClassVar, overload
from java.nio.ByteBuffer import ByteBuffer

class ReadableByteChannel:
    def read(self, arg0: ByteBuffer) -> int: ...
