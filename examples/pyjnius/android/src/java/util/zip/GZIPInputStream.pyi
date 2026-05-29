from typing import Any, ClassVar, overload
from java.io.InputStream import InputStream
from java.util.zip.CRC32 import CRC32

class GZIPInputStream:
    GZIP_MAGIC: ClassVar[int]
    crc: CRC32
    eos: bool
    @overload
    def __init__(self, arg0: InputStream, arg1: int) -> None: ...
    @overload
    def __init__(self, arg0: InputStream) -> None: ...
    def read(self, arg0: list[int], arg1: int, arg2: int) -> int: ...
    def close(self) -> None: ...
