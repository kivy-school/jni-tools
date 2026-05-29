from typing import Any, ClassVar, overload
from java.nio.charset.Charset import Charset
from java.util.Iterator import Iterator

class CharsetProvider:
    def charsetForName(self, p0: str) -> Charset: ...
    def charsets(self) -> Iterator: ...
