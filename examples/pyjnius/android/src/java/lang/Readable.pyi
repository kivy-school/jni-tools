from typing import Any, ClassVar, overload
from java.nio.CharBuffer import CharBuffer

class Readable:
    def read(self, arg0: CharBuffer) -> int: ...
