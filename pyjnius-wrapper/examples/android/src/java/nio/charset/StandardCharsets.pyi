from typing import Any, ClassVar, overload
from java.nio.charset.Charset import Charset

class StandardCharsets:
    ISO_8859_1: ClassVar[Charset]
    US_ASCII: ClassVar[Charset]
    UTF_16: ClassVar[Charset]
    UTF_16BE: ClassVar[Charset]
    UTF_16LE: ClassVar[Charset]
    UTF_8: ClassVar[Charset]
