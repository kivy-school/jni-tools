from typing import Any, ClassVar, overload
from java.nio.ByteBuffer import ByteBuffer

class WritableByteChannel:
    def write(self, p0: ByteBuffer) -> int: ...
