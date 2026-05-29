from typing import Any, ClassVar, overload
from java.nio.charset.Charset import Charset

class StandardCharsets:
    US_ASCII: ClassVar[Charset]
    ISO_8859_1: ClassVar[Charset]
    UTF_8: ClassVar[Charset]
    UTF_16BE: ClassVar[Charset]
    UTF_16LE: ClassVar[Charset]
    UTF_16: ClassVar[Charset]
    UTF_32BE: ClassVar[Charset]
    UTF_32LE: ClassVar[Charset]
    UTF_32: ClassVar[Charset]
